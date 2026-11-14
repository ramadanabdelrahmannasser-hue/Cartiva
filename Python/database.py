from sqlalchemy import create_engine
from getpass import getpass
from urllib.parse import quote_plus


def create_db_engine(database_name="ecommerce_product_analytics"):
    username = "root"
    password = quote_plus(getpass("Enter MySQL Password: "))

    host = "localhost"
    database = database_name

    engine = create_engine(
        f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
    )

    return engine   