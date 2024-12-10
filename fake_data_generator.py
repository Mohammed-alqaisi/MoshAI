# from faker import Faker
# import random
# from sqlalchemy import create_engine
# from datetime import datetime, timedelta
# import os
# from dotenv import load_dotenv
# from sqlalchemy import text

# # Load environment variables
# load_dotenv()

# DB_USERNAME = os.getenv('DB_USERNAME')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT')
# DB_NAME = os.getenv('DB_NAME')

# # Initialize Faker
# fake = Faker()

# # PostgreSQL connection
# def create_connection():
#     engine = create_engine(f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
#     return engine

# # Generate and format dates in YYYY-MM-DD format
# def generate_date():
#     return fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d")

# # Generate fake client_list data
# def generate_client_list_data(num_clients):
#     client_list = []
#     for _ in range(num_clients):
#         client_name = fake.company()
#         contact = fake.email()
#         industry = random.choice(["Construction", "Technology", "Retail", "Manufacturing", "Healthcare"])
#         address = fake.address().replace("\n", ", ")
#         action = random.choice(["View", "Edit", "Delete"])
#         client_list.append((client_name, contact, industry, address, action))
#     return client_list

# # Generate fake quotations and sales_order_list data
# def generate_quotation_and_sales_order_data(client_list, num_entries):
#     quotations = []
#     sales_orders = []

#     for _ in range(num_entries):
#         client_name = random.choice(client_list)[0]  # Match client_name from client_list
#         created_by = fake.name()
#         creation_date = generate_date()
#         quotation_id = f"QC{random.randint(10, 99)}-RZ-QUO{str(random.randint(1000, 9999)).zfill(4)}"
#         assigned_to = fake.first_name()
#         approval_status = random.choice(["Pending", "Approved", "Rejected"])
#         pending_with = fake.first_name()
#         quotation_status = random.choice(["Open", "Closed"])
#         sales_order = quotation_id  # Maintain the relationship with quotations

#         # Add to quotations
#         quotations.append((quotation_id, created_by, creation_date, client_name, assigned_to, approval_status, pending_with, quotation_status, sales_order))

#         # Generate sales order details
#         so_status = random.choice(["Pending", "Approved", "Rejected"])
#         requested_date = (datetime.strptime(creation_date, "%Y-%m-%d") + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
#         actual_date = (
#             (datetime.strptime(requested_date, "%Y-%m-%d") + timedelta(days=random.randint(1, 10))).strftime("%Y-%m-%d")
#             if so_status == "Approved"
#             else None
#         )
#         delivery_status = random.choice(["Delivered", "In Progress", "Not Delivered"]) if so_status == "Approved" else "Not Delivered"

#         # Add to sales_orders
#         sales_orders.append((sales_order, created_by, creation_date, client_name, so_status, requested_date, actual_date, delivery_status))

#     return quotations, sales_orders

# # Insert data into the database
# def insert_data_to_db(client_list, quotations, sales_orders):
#     try:
#         engine = create_connection()
#         with engine.begin() as connection:  # Use begin() to commit automatically
#             # Insert into client_list
#             client_list_query = text(
#                 "INSERT INTO moshtriat.client_list (client_name, contact, industry, address, action) "
#                 "VALUES (:client_name, :contact, :industry, :address, :action)"
#             )
#             connection.execute(client_list_query, [
#                 {
#                     "client_name": client[0],
#                     "contact": client[1],
#                     "industry": client[2],
#                     "address": client[3],
#                     "action": client[4],
#                 }
#                 for client in client_list
#             ])

#             # Insert into quotations
#             quotations_query = text(
#                 "INSERT INTO moshtriat.quotations (quotation_id, created_by, creation_date, client_name, assigned_to, approval_status, pending_with, quotation_status, sales_order) "
#                 "VALUES (:quotation_id, :created_by, :creation_date, :client_name, :assigned_to, :approval_status, :pending_with, :quotation_status, :sales_order)"
#             )
#             connection.execute(quotations_query, [
#                 {
#                     "quotation_id": quotation[0],
#                     "created_by": quotation[1],
#                     "creation_date": quotation[2],
#                     "client_name": quotation[3],
#                     "assigned_to": quotation[4],
#                     "approval_status": quotation[5],
#                     "pending_with": quotation[6],
#                     "quotation_status": quotation[7],
#                     "sales_order": quotation[8],
#                 }
#                 for quotation in quotations
#             ])

#             # Insert into sales_order_list
#             sales_orders_query = text(
#                 "INSERT INTO moshtriat.sales_order_list (sales_order, created_by, creation_date, client_name, so_status, requested_date, actual_date, delivery_status) "
#                 "VALUES (:sales_order, :created_by, :creation_date, :client_name, :so_status, :requested_date, :actual_date, :delivery_status)"
#             )
#             connection.execute(sales_orders_query, [
#                 {
#                     "sales_order": sales_order[0],
#                     "created_by": sales_order[1],
#                     "creation_date": sales_order[2],
#                     "client_name": sales_order[3],
#                     "so_status": sales_order[4],
#                     "requested_date": sales_order[5],
#                     "actual_date": sales_order[6],
#                     "delivery_status": sales_order[7],
#                 }
#                 for sales_order in sales_orders
#             ])
#         print("Data inserted successfully!")
#     except Exception as e:
#         print(f"Error inserting data: {e}")

# # Main function
# def main():
#     print("Generating and inserting fake data into the database...")
#     num_clients = 20  # Number of clients to generate
#     num_entries = 100  # Number of quotations and sales orders to generate

#     # Generate data
#     client_list = generate_client_list_data(num_clients)
#     quotations, sales_orders = generate_quotation_and_sales_order_data(client_list, num_entries)

#     # Insert data into the database
#     insert_data_to_db(client_list, quotations, sales_orders)

# if __name__ == "__main__":
#     main()




from faker import Faker
import random
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from sqlalchemy import text
import psycopg2
import datetime

load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Initialize Faker
fake = Faker()

# Connect to PostgreSQL
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = connection.cursor()

# Helper functions
def random_date_within_4_years():
    start_date = datetime.datetime.now() - datetime.timedelta(days=4 * 365)
    end_date = datetime.datetime.now()
    return start_date + (end_date - start_date) * random.random()

def random_purchase_order():
    return f"PO{random.randint(10000, 99999)}"

def random_vendor_account():
    return f"V{random.randint(10000, 99999)}"

def random_line_status():
    return random.choice(["open", "closed", "received"])

def random_currency():
    return random.choice(["QAR", "USD", "EUR", "GBP", "INR"])

def calculate_amount_in_qar(amount, currency):
    exchange_rates = {"QAR": 1, "USD": 3.65, "EUR": 4.0, "GBP": 4.5, "INR": 0.05}
    return amount * exchange_rates[currency]

# Data generation
def generate_fake_data(n):
    fake_data = []
    for _ in range(n):
        quantity = random.randint(1, 1000)
        unit_price = round(random.uniform(1, 200), 2)
        net_amount = quantity * unit_price
        received_qty = random.randint(max(0, quantity - 10), quantity + 10)
        deliver_reminder = received_qty - quantity
        line_status = random_line_status()
        invoiced_qty = received_qty if line_status == "closed" else 0
        currency = random_currency()
        amount_in_qar = calculate_amount_in_qar(net_amount, currency)

        fake_data.append({
            "line_number": random.randint(100, 200),
            "created_date_time": random_date_within_4_years(),
            "purchase_order": random_purchase_order(),
            "vendor_account": random_vendor_account(),
            "name": random.choice(["Company A", "Company B", "Company C", "Company D"]),
            "item_number": f"RM{random.randint(10000, 99999)}",
            "product_name": random.choice(["Product X", "Product Y", "Product Z"]),
            "quantity": quantity,
            "unit_price": unit_price,
            "net_amount": net_amount,
            "line_status": line_status,
            "received_qty": received_qty,
            "deliver_reminder": deliver_reminder,
            "invoiced_qty": invoiced_qty,
            "invoice_reminder": received_qty,
            "currency": currency,
            "amount_in_qar": amount_in_qar,
            "color": random.choice(["Red", "Blue", "Green", "Yellow"]),
            "size": random.choice(["S", "M", "L", "XL"]),
            "style": random.choice(["A", "B", "C"]),
            "version": random.choice(["v1", "v2", "v3"]),
            "configuration": random.choice(["Conf1", "Conf2", "Conf3"]),
            "batch_number": random.randint(1000, 9999),
            "serial_number": random.randint(100000, 999999),
            "cost_center": random.choice(["CC1", "CC2", "CC3"])
        })
    return fake_data

def add_columns_to_table():
    # Define the columns to be added and their data types
    columns = {
        "line_number": "INTEGER",
        "created_date_time": "TIMESTAMP",
        "purchase_order": "VARCHAR(20)",
        "vendor_account": "VARCHAR(20)",
        "name": "VARCHAR(255)",
        "item_number": "VARCHAR(20)",
        "product_name": "VARCHAR(255)",
        "quantity": "INTEGER",
        "unit_price": "NUMERIC(10, 2)",
        "net_amount": "NUMERIC(10, 2)",
        "line_status": "VARCHAR(20)",
        "received_qty": "INTEGER",
        "deliver_reminder": "INTEGER",
        "invoiced_qty": "INTEGER",
        "invoice_reminder": "INTEGER",
        "currency": "VARCHAR(10)",
        "amount_in_qar": "NUMERIC(10, 2)",
        "color": "VARCHAR(20)",
        "size": "VARCHAR(5)",
        "style": "VARCHAR(5)",
        "version": "VARCHAR(5)",
        "configuration": "VARCHAR(10)",
        "batch_number": "INTEGER",
        "serial_number": "INTEGER",
        "cost_center": "VARCHAR(50)"
    }

    # Loop through columns and add them if they don't exist
    for column_name, column_type in columns.items():
        cursor.execute(f"""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'invoice' AND column_name = '{column_name}'
                ) THEN
                    ALTER TABLE erp.invoice ADD COLUMN {column_name} {column_type};
                END IF;
            END
            $$;
        """)
    connection.commit()

# Insert data into PostgreSQL
def insert_data_into_db(data):
    for record in data:
        cursor.execute("""
            INSERT INTO erp.invoice (
                line_number, created_date_time, purchase_order, vendor_account, name, item_number, 
                product_name, quantity, unit_price, net_amount, line_status, received_qty, 
                deliver_reminder, invoiced_qty, invoice_reminder, currency, amount_in_qar, color, 
                size, style, version, configuration, batch_number, serial_number, cost_center
            ) VALUES (
                %(line_number)s, %(created_date_time)s, %(purchase_order)s, %(vendor_account)s, %(name)s, %(item_number)s, 
                %(product_name)s, %(quantity)s, %(unit_price)s, %(net_amount)s, %(line_status)s, %(received_qty)s, 
                %(deliver_reminder)s, %(invoiced_qty)s, %(invoice_reminder)s, %(currency)s, %(amount_in_qar)s, %(color)s, 
                %(size)s, %(style)s, %(version)s, %(configuration)s, %(batch_number)s, %(serial_number)s, %(cost_center)s
            )
        """, record)
    connection.commit()

# Generate and insert fake data
add_columns_to_table()
fake_data = generate_fake_data(8500)  # Adjust the number of rows as needed
insert_data_into_db(fake_data)

# Close connection
cursor.close()
connection.close()
# Define and create the ERP schema
# tables = {
#     "employees": """
#         CREATE TABLE IF NOT EXISTS erp.employees (
#             employee_id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             email VARCHAR(100),
#             department_id INT,
#             hire_date DATE,
#             salary NUMERIC
#         )
#     """,
#     "departments": """
#         CREATE TABLE IF NOT EXISTS erp.departments (
#             department_id SERIAL PRIMARY KEY,
#             department_name VARCHAR(100)
#         )
#     """,
#     "clients": """
#         CREATE TABLE IF NOT EXISTS erp.clients (
#             client_id SERIAL PRIMARY KEY,
#             client_name VARCHAR(100),
#             contact VARCHAR(15),
#             industry VARCHAR(50),
#             address TEXT
#         )
#     """,
#     "quotations": """
#         CREATE TABLE IF NOT EXISTS erp.quotations (
#             quotation_id SERIAL PRIMARY KEY,
#             client_id INT,
#             created_by INT,
#             creation_date DATE,
#             total_amount NUMERIC
#         )
#     """,
#     "sales_orders": """
#         CREATE TABLE IF NOT EXISTS erp.sales_orders (
#             sales_order_id SERIAL PRIMARY KEY,
#             quotation_id INT,
#             client_id INT,
#             creation_date DATE,
#             delivery_date DATE,
#             status VARCHAR(20)
#         )
#     """,
#     "inventory": """
#         CREATE TABLE IF NOT EXISTS erp.inventory (
#             inventory_id SERIAL PRIMARY KEY,
#             product_id INT,
#             stock_quantity INT
#         )
#     """,
#     "products": """
#         CREATE TABLE IF NOT EXISTS erp.products (
#             product_id SERIAL PRIMARY KEY,
#             product_name VARCHAR(100),
#             price NUMERIC
#         )
#     """,
#     "transactions": """
#         CREATE TABLE IF NOT EXISTS erp.transactions (
#             transaction_id SERIAL PRIMARY KEY,
#             sales_order_id INT,
#             transaction_date DATE,
#             total_amount NUMERIC
#         )
#     """
# }

# # Create tables
# for table, ddl in tables.items():
#     cursor.execute(ddl)

# # Commit table creation
# connection.commit()

# # Initialize placeholders for relationships
# client_ids = []
# employee_ids = []
# department_ids = []
# product_ids = []
# quotation_ids = []
# sales_order_ids = []

# # Populate departments table
# def populate_departments(n=10):
#     global department_ids
#     for _ in range(n):
#         department_name = fake.job()
#         cursor.execute(
#             "INSERT INTO erp.departments (department_name) VALUES (%s) RETURNING department_id", 
#             (department_name,)
#         )
#         department_ids.append(cursor.fetchone()[0])

# # Populate employees table
# def populate_employees(n=50):
#     global employee_ids
#     for _ in range(n):
#         name = fake.name()
#         email = fake.email()
#         department_id = random.choice(department_ids)
#         hire_date = fake.date_this_decade()
#         salary = round(random.uniform(30000, 120000), 2)
#         cursor.execute(
#             "INSERT INTO erp.employees (name, email, department_id, hire_date, salary) VALUES (%s, %s, %s, %s, %s) RETURNING employee_id",
#             (name, email, department_id, hire_date, salary)
#         )
#         employee_ids.append(cursor.fetchone()[0])

# # Populate clients table
# def populate_clients(n=30):
#     global client_ids
#     for _ in range(n):
#         client_name = fake.company()
#         contact = fake.phone_number()[:8]
#         industry = fake.random_element(elements=["Healthcare", "Finance", "Technology", "Retail", "Education", "Manufacturing", "Transportation", "Energy"])
#         address = fake.address()
#         cursor.execute(
#             "INSERT INTO erp.clients (client_name, contact, industry, address) VALUES (%s, %s, %s, %s) RETURNING client_id",
#             (client_name, contact, industry, address)
#         )
#         client_ids.append(cursor.fetchone()[0])

# # Populate products table
# def populate_products(n=20):
#     global product_ids
#     for _ in range(n):
#         product_name = fake.word().capitalize()
#         price = round(random.uniform(50, 1000), 2)
#         cursor.execute(
#             "INSERT INTO erp.products (product_name, price) VALUES (%s, %s) RETURNING product_id",
#             (product_name, price)
#         )
#         product_ids.append(cursor.fetchone()[0])

# # Populate inventory table
# def populate_inventory():
#     for product_id in product_ids:
#         stock_quantity = random.randint(10, 500)
#         cursor.execute(
#             "INSERT INTO erp.inventory (product_id, stock_quantity) VALUES (%s, %s)",
#             (product_id, stock_quantity)
#         )

# # Populate quotations table
# def populate_quotations(n=50):
#     global quotation_ids
#     for _ in range(n):
#         client_id = random.choice(client_ids)
#         created_by = random.choice(employee_ids)
#         creation_date = fake.date_this_year()
#         total_amount = round(random.uniform(1000, 50000), 2)
#         cursor.execute(
#             "INSERT INTO erp.quotations (client_id, created_by, creation_date, total_amount) VALUES (%s, %s, %s, %s) RETURNING quotation_id",
#             (client_id, created_by, creation_date, total_amount)
#         )
#         quotation_ids.append(cursor.fetchone()[0])

# # Populate sales_orders table
# def populate_sales_orders(n=50):
#     global sales_order_ids
#     for _ in range(n):
#         quotation_id = random.choice(quotation_ids)
#         client_id = random.choice(client_ids)
#         creation_date = fake.date_this_year()
#         delivery_date = fake.date_this_year()
#         status = random.choice(['Pending', 'Completed', 'Cancelled'])
#         cursor.execute(
#             "INSERT INTO erp.sales_orders (quotation_id, client_id, creation_date, delivery_date, status) VALUES (%s, %s, %s, %s, %s) RETURNING sales_order_id",
#             (quotation_id, client_id, creation_date, delivery_date, status)
#         )
#         sales_order_ids.append(cursor.fetchone()[0])

# # Populate transactions table
# def populate_transactions(n=50):
#     for _ in range(n):
#         sales_order_id = random.choice(sales_order_ids)
#         transaction_date = fake.date_this_year()
#         total_amount = round(random.uniform(500, 10000), 2)
#         cursor.execute(
#             "INSERT INTO erp.transactions (sales_order_id, transaction_date, total_amount) VALUES (%s, %s, %s)",
#             (sales_order_id, transaction_date, total_amount)
#         )

# # Call the population functions in the correct order
# populate_departments()
# populate_employees()
# populate_clients()
# populate_products()
# populate_inventory()
# populate_quotations()
# populate_sales_orders()
# populate_transactions()

# # Commit data insertion
# connection.commit()

# # Close connection
# cursor.close()
# connection.close()