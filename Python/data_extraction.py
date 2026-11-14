import pandas as pd
from sqlalchemy import inspect
from database import create_db_engine

# Establish a connection to the database
engine = create_db_engine()

# Retrieve all table names from the database schema
inspector = inspect(engine)
table_names = inspector.get_table_names()

# Initialize a dictionary to store the DataFrames
dataframes = {}

# Extract each table and store it as a DataFrame within the dictionary
for table in table_names:
    query = f"SELECT * FROM {table}"
    dataframes[table] = pd.read_sql(query, con=engine)

# Terminate the database connection to free up resources
engine.dispose()

# ----------------------------------------------------
# Verify the loaded data (Accessing via the dictionary keys)
print(dataframes['users'].head())
print(dataframes['orders'].info())