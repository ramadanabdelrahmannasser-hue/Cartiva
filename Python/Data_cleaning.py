import pandas as pd
from data_extraction import dataframes

# ==========================================
# 1. Sessions Transformation
# ==========================================
Dim_sessions = dataframes["sessions"].copy()

# Standardize traffic source naming
Dim_sessions["traffic_source"] = Dim_sessions["traffic_source"].replace(
    "Social", "Paid Social"
)

# Drop redundant columns
Dim_sessions = Dim_sessions.drop(columns=["traffic_medium"])


# ==========================================
# 2. Users Transformation
# ==========================================
Dim_users = dataframes["users"].copy()

# Standardize acquisition source naming
Dim_users["acquisition_source"] = Dim_users["acquisition_source"].replace(
    "Social", "Paid Social"
)

# Drop redundant columns
Dim_users = Dim_users.drop(columns=["acquisition_medium"])


# ==========================================
# 3. Events Transformation
# ==========================================
Fact_Events = dataframes["events"].copy()

# Convert event_timestamp to datetime object
Fact_Events["event_timestamp"] = pd.to_datetime(
    Fact_Events["event_timestamp"]
)

# Split timestamp into separate date and time columns
Fact_Events["event_date"] = Fact_Events["event_timestamp"].dt.date
Fact_Events["event_time"] = Fact_Events["event_timestamp"].dt.time

# Drop the original combined timestamp column
Fact_Events = Fact_Events.drop(columns=["event_timestamp"])


# ==========================================
# 4. Fact Sales Creation & Transformation
# ==========================================
Fact_Sales = pd.merge(
    dataframes["orders"],
    dataframes["order_items"],
    on="order_id",
    how="inner"
)

# Select relevant attributes
Fact_Sales = Fact_Sales[
    [
        "order_item_id",
        "order_id",
        "user_id",
        "session_id",
        "product_id",
        "order_date",
        "order_status",
        "quantity",
        "unit_price"
    ]
].copy()

# Calculate item-level revenue
Fact_Sales["line_amount"] = (
    Fact_Sales["quantity"] * Fact_Sales["unit_price"]
)

# Split order_date into separate date and time columns
Fact_Sales["order_date"] = pd.to_datetime(Fact_Sales["order_date"])
Fact_Sales["order_time"] = Fact_Sales["order_date"].dt.time
Fact_Sales["order_date"] = Fact_Sales["order_date"].dt.date


# ==========================================
# 5. Consolidate Transformed DataFrames
# ==========================================
transformed_dataframes = {
    "dim_sessions": Dim_sessions,
    "dim_users": Dim_users,
    "dim_products": dataframes["products"].copy(),
    "fact_sales": Fact_Sales,
    "fact_events": Fact_Events
}


# ==========================================
# 6. Verify Final DataFrames
# ==========================================
for table_name, df in transformed_dataframes.items():
    print(f"Table: {table_name} | Shape: {df.shape}")
for table_name, df in transformed_dataframes.items():
    print(f"\n{table_name}")
    print("Duplicate Rows:", df.duplicated().sum())
    print("Missing Values:", df.isnull().sum().sum())    
print(Fact_Events.isnull().sum())   