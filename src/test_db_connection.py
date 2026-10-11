import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


# locate the .env file in the project root directory.

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env") # Load environment variables from the .env file in the project root directory.

# Read the database settings.
connection_url = URL.create( # URL.create() method builds the connection details safely, including password.
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME")
)

# create the connection engine.
engine = create_engine(connection_url) # create_engine() prepares SQLAlchemy to connect to PostgreSQL.

# Test the database connection and indentify the connected database.

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user;") # check which database and user the connection reaches.
            )
        database_name, username = result.fetchone()
        print(f"Successfully connected to the database: {database_name}")
        print(f"Connected as user: {username}")
except Exception as error:
    print(f"Error connecting to the database: {error}") 

finally:
    engine.dispose()  # Close the connection engine.
