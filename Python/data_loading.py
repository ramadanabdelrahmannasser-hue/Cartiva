from database import create_db_engine
from Data_cleaning import transformed_dataframes

# Connect to the Data Warehouse
engine = create_db_engine("ecommerce_product_analytics_dw")

# Load transformed DataFrames into MySQL
for table_name, df in transformed_dataframes.items():

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully!")

engine.dispose()