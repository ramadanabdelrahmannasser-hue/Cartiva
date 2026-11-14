import mysql.connector
from getpass import getpass
import random
from datetime import timedelta

random.seed(42)

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("MySQL Password: "),
    database="ecommerce_product_analytics"
)

cursor = connection.cursor()

# ---------------------------------
# 1. Load checkout sessions
# ---------------------------------

cursor.execute("""
    SELECT
        s.session_id,
        s.user_id,
        s.session_start,
        s.session_end,
        MAX(e.event_timestamp) AS last_event_time
    FROM sessions s
    JOIN events e
        ON s.session_id = e.session_id
    WHERE e.event_name = 'begin_checkout'
    GROUP BY
        s.session_id,
        s.user_id,
        s.session_start,
        s.session_end
""")

checkout_sessions = cursor.fetchall()

print("Checkout sessions:", len(checkout_sessions))

# ---------------------------------
# 2. Select 5000 sessions
# ---------------------------------

if len(checkout_sessions) < 5000:
    raise ValueError("Not enough checkout sessions!")

selected_sessions = random.sample(checkout_sessions, 5000)

# ---------------------------------
# 3. Load products
# ---------------------------------

cursor.execute("""
    SELECT product_id, price
    FROM products
""")

products = cursor.fetchall()

orders = []
order_items = []
purchase_events = []

order_id = 1
order_item_id = 1

# Get next event ID
cursor.execute("SELECT MAX(event_id) FROM events")
max_event_id = cursor.fetchone()[0] or 0

event_id = max_event_id + 1

# ---------------------------------
# 4. Generate orders and items
# ---------------------------------

for session in selected_sessions:

    session_id, user_id, session_start, session_end, last_event = session

    # Purchase happens after the last existing event
    purchase_time = session_end - timedelta(seconds=1)

    # Generate 1-3 products per order
    number_of_items = random.randint(1, 3)

    selected_products = random.sample(
        products,
        number_of_items
    )

    total_amount = 0

    for product_id, price in selected_products:

        quantity = random.randint(1, 3)

        line_total = price * quantity

        total_amount += line_total

        order_items.append((
            order_item_id,
            order_id,
            product_id,
            quantity,
            price
        ))

        order_item_id += 1

    # Order status
    status = random.choices(
        ["Completed", "Cancelled", "Refunded"],
        weights=[0.90, 0.05, 0.05]
    )[0]

    orders.append((
        order_id,
        user_id,
        session_id,
        purchase_time,
        status,
        round(total_amount, 2)
    ))

    # Purchase event linked to the actual order session
    purchase_events.append((
        event_id,
        session_id,
        user_id,
        "purchase",
        purchase_time,
        None
    ))

    order_id += 1
    event_id += 1


# ---------------------------------
# 5. Insert orders
# ---------------------------------

cursor.executemany("""
    INSERT INTO orders (
        order_id,
        user_id,
        session_id,
        order_date,
        order_status,
        total_amount
    )
    VALUES (%s, %s, %s, %s, %s, %s)
""", orders)

connection.commit()

print("Inserted orders:", len(orders))


# ---------------------------------
# 6. Insert order items
# ---------------------------------

cursor.executemany("""
    INSERT INTO order_items (
        order_item_id,
        order_id,
        product_id,
        quantity,
        unit_price
    )
    VALUES (%s, %s, %s, %s, %s)
""", order_items)

connection.commit()

print("Inserted order items:", len(order_items))


# ---------------------------------
# 7. Insert purchase events
# ---------------------------------

cursor.executemany("""
    INSERT INTO events (
        event_id,
        session_id,
        user_id,
        event_name,
        event_timestamp,
        product_id
    )
    VALUES (%s, %s, %s, %s, %s, %s)
""", purchase_events)

connection.commit()

print("Inserted purchase events:", len(purchase_events))

cursor.close()
connection.close()

print("Order generation completed successfully!")