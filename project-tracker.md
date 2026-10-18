# Finance Analytics Platform — Project Tracker

## Project Status

**Project:** Real-Time Multi-Asset Financial Analytics & Risk Intelligence Platform

**Status:** In Progress

**Started:** October 2026

**GitHub Repository:** [Add repository link]

---

# 1. Project Objective

Build an end-to-end financial analytics platform that collects frequently updated financial and macroeconomic data, performs data cleaning, validation and feature engineering, stores the data in PostgreSQL, uses Apache Hop for ETL/EDA workflows, and presents portfolio performance, risk and macroeconomic insights through Power BI.

---

# 2. Technology Stack

| Technology | Purpose | Status |
|---|---|---|
| Python | Data ingestion, cleaning, validation and feature engineering | Not started |
| Pandas | Data manipulation | Not started |
| NumPy | Numerical calculations | Not started |
| PostgreSQL | Data storage | Not started |
| Apache Hop | ETL / data workflows / EDA | Not started |
| SciPy | Statistical testing | Not started |
| Statsmodels | Regression/statistical analysis | Not started |
| Power BI | Dashboard and visualization | Not started |
| DAX | Power BI measures | Not started |
| Git/GitHub | Version control | In progress |
| pytest | Testing | Not started |

---

# 3. Project Data

## Asset Universe

### Technology
- AAPL
- MSFT
- NVDA
- GOOGL
- META

### Financial
- JPM
- BAC

### Healthcare
- JNJ
- UNH

### Energy
- XOM

### Cryptocurrency
- BTC-USD
- ETH-USD

### Benchmark
- S&P 500 (^GSPC)

## Macroeconomic Data

- Federal Funds Rate
- CPI
- Unemployment Rate
- GDP
- 3-Month Treasury Rate

---

# 4. Data Sources

| Dataset | Source | Status |
|---|---|---|
| Stock prices | Yahoo Finance | Not started |
| Cryptocurrency prices | Yahoo Finance | Not started |
| S&P 500 | Yahoo Finance | Not started |
| Federal Funds Rate | FRED | Not started |
| CPI | FRED | Not started |
| Unemployment | FRED | Not started |
| GDP | FRED | Not started |
| Treasury Rate | FRED | Not started |
| Company financial statements | SEC EDGAR | Not started |

---

# 5. Project Milestones

Milestone 1 — Project Definition
- [x] Project idea finalized
- [x] Initial scope defined
- [x] Asset universe defined
- [x] Initial data sources defined
- [x] Technology stack defined
- [x] GitHub repository created
- [x] Project tracker created


Milestone 2 — Development Environment
- [x] Python 3.14.6 available
- [x] Git installed
- [x] Git verified
- [x] Local repository cloned
- [x] Python verified
- [x] pip verified
- [x] Virtual environment created
- [x] Virtual environment activated
- [x] Virtual environment verified
- [x] Core Python libraries installed
- [x] Initial project structure created
- [x] Git tracking verified
- [x] Git identity configured
- [x] First project commit created
- [x] Initial project structure pushed to GitHub

- [x] PostgreSQL installed
- [x] PostgreSQL configured
- [ ] Apache Hop installed
- [ ] Power BI Desktop installed

## Milestone 3 — Data Acquisition

- [ ] Market data source connection tested
- [ ] First asset data retrieved
- [ ] Raw data saved
- [ ] Data structure inspected
- [ ] Historical period verified
- [ ] All selected assets retrieved
- [ ] FRED data retrieved
- [ ] Data acquisition documented

## Milestone 4 — Data Cleaning

- [ ] Column names standardized
- [ ] Data types validated
- [ ] Dates standardized
- [ ] Missing values investigated
- [ ] Duplicate records checked
- [ ] Invalid prices checked
- [ ] Invalid volume checked
- [ ] Corporate actions considered
- [ ] Cleaning process documented

## Milestone 5 — Data Validation

- [ ] Completeness checks
- [ ] Uniqueness checks
- [ ] Validity checks
- [ ] Consistency checks
- [ ] Referential integrity checks
- [ ] Timeliness checks
- [ ] Validation framework created
- [ ] Failed records/rejections handled

## Milestone 6 — Feature Engineering

- [ ] Daily returns
- [ ] Weekly returns
- [ ] Monthly returns
- [ ] Rolling volatility
- [ ] Moving averages
- [ ] Momentum
- [ ] RSI
- [ ] MACD
- [ ] Maximum drawdown
- [ ] Sharpe Ratio
- [ ] Sortino Ratio
- [ ] VaR
- [ ] Beta
- [ ] Rolling correlations
- [ ] Macro features
- [ ] Market regime features

## Milestone 7 — PostgreSQL

- [ ] Database created
- [ ] Schemas created
- [ ] Dimension tables created
- [ ] Fact tables created
- [ ] Raw data loaded
- [ ] Clean data loaded
- [ ] Feature data loaded
- [ ] Indexes considered
- [ ] ETL audit table created

## Milestone 8 — Apache Hop

- [ ] Hop environment configured
- [ ] Database connection created
- [ ] Market data workflow
- [ ] Macro data workflow
- [ ] Data quality workflow
- [ ] Feature engineering workflow
- [ ] Transformation workflows
- [ ] Workflow documentation

## Milestone 9 — Statistical Analysis

- [ ] Descriptive statistics
- [ ] Correlation analysis
- [ ] Pearson correlation tests
- [ ] T-tests
- [ ] Confidence intervals
- [ ] Regression analysis
- [ ] Regression diagnostics
- [ ] Sharpe analysis
- [ ] VaR analysis
- [ ] Portfolio risk analysis

## Milestone 10 — Power BI

- [ ] PostgreSQL connection
- [ ] Data model
- [ ] Date dimension
- [ ] Asset dimension
- [ ] Relationships
- [ ] DAX measures
- [ ] Executive dashboard
- [ ] Performance page
- [ ] Risk page
- [ ] Correlation page
- [ ] Macro page
- [ ] Sector page
- [ ] Portfolio page
- [ ] Slicers and filters
- [ ] Refresh strategy

## Milestone 11 — Automation

- [ ] Incremental data ingestion
- [ ] Scheduled refresh
- [ ] Pipeline logging
- [ ] Error handling
- [ ] ETL audit tracking
- [ ] Power BI refresh strategy

## Milestone 12 — Finalization

- [ ] Unit tests
- [ ] Data dictionary
- [ ] Architecture documentation
- [ ] Methodology documentation
- [ ] Final statistical report
- [ ] GitHub README completed
- [ ] Dashboard screenshots
- [ ] Final project review
- [ ] Resume project description
- [ ] Interview explanation prepared

---

# 6. Decision Log

| Date | Decision | Reason |
|---|---|---|
| October 2026 | Use Python for ingestion and feature engineering | Core analytical/data processing layer |
| October 2026 | Use PostgreSQL as central database | Structured analytical storage |
| October 2026 | Use Apache Hop for ETL/EDA workflows | Visual workflow and ETL layer |
| October 2026 | Use Power BI for final dashboard | Business-facing analytics layer |
| October 2026 | Start with 5 years of historical data | Sufficient observations for analysis |
| October 2026 | Begin with controlled asset universe | Prevent project scope from becoming unmanageable |

---

# 7. Problems / Issues Encountered

| Date | Problem | Solution | Status |
|---|---|---|---|
| | | | |

---

# 8. Important Concepts Learned

| Date | Concept | My Understanding |
|---|---|---|
| | | |

---

# 9. Git Commit History

| Date | Commit | What Changed |
|---|---|---|
| | | |

---

# 10. Current Position

**Completed:** GitHub repository creation

### Progress Update — 11 October 2026

**Completed**
- Downloaded and inspected five years of AAPL market data using Python.
- Checked missing values, duplicate dates, date ordering, price validity, and negative volume.
- Created the `raw.market_prices` PostgreSQL table.
- Configured database credentials in `.env` and confirmed `.env` is listed in `.gitignore`.
- Successfully tested the Python-to-PostgreSQL connection.

**Technical issue resolved**
- SQLAlchemy 2.1.3 failed to import because Windows Application Control blocked a compiled component.
- Changed SQLAlchemy to version 2.0.43.
- Confirmed that Python can connect to the `finance-analytics` database as `postgres`.



### Progress Update — 12 October 2026

**Completed**
- Created a reusable Python function to fetch historical market data using yfinance.
- Implemented data-quality checks for missing values, duplicate dates, date ordering, invalid prices, and negative volume.
- Created a database engine using SQLAlchemy and credentials loaded from `.env`.
- Implemented a data-preparation function to align Yahoo Finance columns with the PostgreSQL schema.
- Implemented repeatable loading using PostgreSQL conflict handling on the `(ticker, trading_date)` primary key.
- Loaded 1,255 AAPL records into `raw.market_prices`.
- Verified the database row count and checked for duplicate ticker-date combinations.
- Corrected a spelling mismatch in the PostgreSQL column name from `dividents` to `dividends`.

**Current architecture**
Yahoo Finance → Python ingestion and preparation → PostgreSQL `raw.market_prices`

**Next milestone**
- Expand ingestion to the remaining assets.
- Make the ingestion process reusable across all configured tickers.
- Verify data coverage and loading behavior for each asset before building the analytical layer.



### Multi-Asset Market Data Ingestion — Completed 18 Oct

**Completed**
- Expanded the Python ingestion pipeline from AAPL to all 13 configured assets.
- Downloaded approximately five years of historical market data using yfinance.
- Applied data-quality checks for missing values, duplicate dates, date ordering, invalid prices, and negative volume.
- Prepared market data for PostgreSQL using a reusable transformation function.
- Loaded or updated records using PostgreSQL upsert logic.
- Processed all 13 tickers successfully, with zero reported ingestion failures.
- Verified that PostgreSQL contains 13 distinct tickers.
- Verified 17,464 stored records across all assets.
- Confirmed zero rows with missing ticker or trading-date values.
- Confirmed that repeatable loading retains earlier records and updates conflicting ticker-date records.

**Current architecture**
Yahoo Finance → Python ingestion → Data validation → Data preparation → PostgreSQL `raw.market_prices`

**Next milestone**
Build the macroeconomic data ingestion pipeline using FRED, including series metadata, observation dates, values, and appropriate handling of different data frequencies.


