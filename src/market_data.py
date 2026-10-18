# Ingestion Code
# Import Library.
import yfinance as yf
import os 
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import MetaData,Table

def create_db_engine():
    """
    Create a SQLAlchemy engine for connecting to the PostgreSQL database.
    """
    # locate the .env file in the project root directory.
    project_root = Path(__file__).resolve().parent.parent
    load_dotenv(project_root / ".env")  # Load environment variables from the .env file in the project root directory.

    # Read the database settings.
    connection_url = URL.create(  # URL.create() method builds the connection details safely, including password.
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME")
    )

    return create_engine(connection_url)

# create a reusable function for downloading data.
def fetch_market_data(ticker: str, period: str="5y"): 
    """
    Here "ticker: str" - indicates that the ticker should be a string, such as "AAPL"
    "period: str="5y"" - Uses five years of history by default.
    Retriving historical market data for a ticker from yahoo finance.
    """
    data = yf.Ticker(ticker).history(
        period = period,
        auto_adjust = False # Requests unadjusted OHLC values and the separate adjusted - close field when provided.
    )

    if data.empty:# check wheather the returned DataFrame contains any row
        raise ValueError(f"No market data returned for ticker: {ticker}")
    return data

def prepare_market_data(data: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """
    Prepare downloaded market data for the raw PostrgeSQL table.
    """
    prepared = data.copy() # Create a copy of the original DataFrame to avoid modifying it directly.
    # convert the date index into a regular column
    prepared = prepared.reset_index() # Reset the index of the DataFrame, moving the date index into a regular column.
    # Rename yahoo finance columns to match PostgreSQL.
    prepared = prepared.rename(
        columns={
            "Date":"trading_date",
            "Datetime":"trading_date",
            "Open":"open_price",
            "High":"high_price",
            "Low":"low_price",
            "Close":"close_price",
            "Adj Close":"adjusted_close",
            "Volume":"volume",
            "Dividends":"dividends",
            "Stock Splits":"stock_splits"
        }
    )
    # Add the ticker to every row.
    prepared["ticker"] = ticker

    # keep only the columns required by the database table.
    prepared = prepared[[
        "ticker",
        "trading_date",
        "open_price",
        "high_price",
        "low_price",
        "close_price",
        "adjusted_close",
        "volume",
        "dividends",
        "stock_splits"
    ]]

    # Convert timestamps to dates for the PostgreSQL Date column.
    prepared["trading_date"] = pd.to_datetime(prepared["trading_date"]).dt.date

    return prepared

# Data Loading 
def load_market_data(
        prepared_data: pd.DataFrame,
        engine,
) -> int:
    """
    Insert or Update prepared market records in PostgreSQL table.

    """
    if prepared_data.empty:
        print("No data to load.")
        return 0
    metadata = MetaData()

    market_prices = Table(
        "market_prices",
        metadata,
        schema="raw",
        autoload_with=engine
    )

    records = prepared_data.to_dict(orient="records")  # Convert the DataFrame to a list of dictionaries, where each dictionary represents a row.

    insert_statement = insert(market_prices).values(records)  # Create an insert statement for the market_prices table with the prepared records.
    #print("DataFrame columns:", prepared_data.columns.tolist())
    #print("Database columns:", list(market_prices.columns.keys()))

    upsert_statement = insert_statement.on_conflict_do_update(
        constraint="pk_market_prices",  # Specify the primary key constraint for conflict resolution.
        set_={
            "open_price": insert_statement.excluded.open_price,
            "high_price": insert_statement.excluded.high_price,
            "low_price": insert_statement.excluded.low_price,
            "close_price": insert_statement.excluded.close_price,
            "adjusted_close": insert_statement.excluded.adjusted_close,
            "volume": insert_statement.excluded.volume,
            "dividends": insert_statement.excluded.dividends,
            "stock_splits": insert_statement.excluded.stock_splits,
            "data_source": insert_statement.excluded.data_source,
        },
    )
    with engine.begin() as connection:  # Use a context manager to handle the database connection and transaction.
        connection.execute(upsert_statement)  # Execute the upsert statement to insert or update records in the market_prices table.

    return len(records)  # Return the number of records processed (inserted or updated).


if __name__ == "__main__":
    tickers = [
        "AAPL",
        "MSFT",
        "NVDA",
        "GOOGL",
        "META",
        "JPM",
        "BAC",
        "JNJ",
        "UNH",
        "XOM",
        "BTC-USD",
        "ETH-USD",
        "^GSPC",
    ]

    print("Connecting to PostgreSQL...")
    engine = create_db_engine()

    successful_tickers = []
    failed_tickers = []

    try:
        with engine.connect() as connection:
            print("Database connection successful.")

        for ticker in tickers:
            print(f"\n{'=' * 50}")
            print(f"Processing ticker: {ticker}")
            print(f"{'=' * 50}")

            try:
                # 1. Download market data.
                market_data = fetch_market_data(ticker)

                print("Rows retrieved:", len(market_data))
                print("Date range:", market_data.index.min(), "to", market_data.index.max())

                # 2. Run data-quality checks.
                print("Missing values:")
                print(market_data.isna().sum())

                print("Duplicate dates:", market_data.index.duplicated().sum())
                print("Date index sorted:", market_data.index.is_monotonic_increasing)

                invalid_prices = (
                    (market_data["High"] < market_data["Low"])
                    | (market_data["High"] < market_data["Open"])
                    | (market_data["High"] < market_data["Close"])
                    | (market_data["Low"] > market_data["Open"])
                    | (market_data["Low"] > market_data["Close"])
                    | (
                        market_data[
                            ["Open", "High", "Low", "Close"]
                        ] <= 0
                    ).any(axis=1)
                )

                negative_volume_rows = (
                    market_data["Volume"] < 0
                ).sum()

                print("Invalid price rows:", invalid_prices.sum())
                print("Negative volume rows:", negative_volume_rows)

                # Stop loading if critical quality checks fail.
                if invalid_prices.any():
                    raise ValueError(
                        f"{ticker} contains invalid price rows."
                    )

                if market_data.index.has_duplicates:
                    raise ValueError(
                        f"{ticker} contains duplicate dates."
                    )

                if not market_data.index.is_monotonic_increasing:
                    raise ValueError(
                        f"{ticker} dates are not sorted."
                    )

                # 3. Prepare data for PostgreSQL.
                prepared_data = prepare_market_data(
                    market_data,
                    ticker,
                )

                print("Prepared rows:", len(prepared_data))

                # 4. Load data into PostgreSQL.
                loaded_rows = load_market_data(
                    prepared_data,
                    engine,
                )

                print(
                    f"Successfully processed {loaded_rows} rows "
                    f"for {ticker}."
                )

                successful_tickers.append(ticker)

            except Exception as error:
                print(f"FAILED: {ticker}")
                print(f"Reason: {error}")
                failed_tickers.append((ticker, str(error)))

    finally:
        engine.dispose()

    # 5. Print the final summary.
    print("\n" + "=" * 50)
    print("INGESTION SUMMARY")
    print("=" * 50)

    print("Total tickers:", len(tickers))
    print("Successful:", len(successful_tickers))
    print("Failed:", len(failed_tickers))

    print("\nSuccessful tickers:")
    for ticker in successful_tickers:
        print("-", ticker)

    if failed_tickers:
        print("\nFailed tickers:")
        for ticker, reason in failed_tickers:
            print(f"- {ticker}: {reason}")




                    



    '''
    market_data = fetch_market_data(ticker)

    print(f"Ticker: {ticker}")
    print(f"Rows retrieved: {len(market_data)}")
    print(
        f"Data range: {market_data.index.min()}"
        f"to {market_data.index.max()}"
    )

    print("\nFirst Five records:")
    print(market_data.head())

    print("\nColumn Names:")
    print(market_data.columns.tolist())

    print("\nData types: ")
    print(market_data.dtypes)

    print("\nMissing Values per column: ")
    print(market_data.isna().sum())

    print("\nDuplicate date: ")
    print(market_data.index.duplicated().sum())

    print("\nDate Index sorted: ")
    print(market_data.index.is_monotonic_increasing)

    print("\nBasic price statistics :")
    print(market_data[['Open', 'High', 'Low', 'Close']].describe())

    print("\nprice validation: ")

    invalid_prices = (
    (market_data["High"] < market_data["Low"])
    | (market_data["High"] < market_data["Open"])
    | (market_data["High"] < market_data["Close"])
    | (market_data["Low"] > market_data["Open"])
    | (market_data["Low"] > market_data["Close"])
    | (market_data[["Open", "High", "Low", "Close"]] <= 0).any(axis=1)
)

    print("Invalid price rows: ", invalid_prices.sum())

    print(
        "negative Volume rows: ",
        (market_data['Volume'] < 0).sum()
    )

    print("\nTesting database engine:")
    engine = create_db_engine()

    try:
        with engine.connect() as connection:
            print("Database engine connection successful.")
    finally:
        engine.dispose()  # Close the connection engine.


    print("\nPreparing market data for PostgreSQL:")
    prepared_data = prepare_market_data(market_data, ticker)
    print("Prepared data:")
    print("Prepared rows: ", len(prepared_data))
    print("Prepared columns: ", prepared_data.columns.tolist())
    print("\nFirst five rows of prepared data:")
    print(prepared_data.head())

    print("\nPrepared data types:")
    print(prepared_data.dtypes)

    print("\nLoading data into PostgreSQL:")

    engine = create_db_engine()  # Create a new database engine for loading data.
    try:
        loaded_rows = load_market_data(prepared_data, engine)  # Load the prepared data into the PostgreSQL database.
        print(f"Successfully loaded {loaded_rows} rows into the database.")
    finally:
        engine.dispose()  # Close the connection engine after loading data.

'''