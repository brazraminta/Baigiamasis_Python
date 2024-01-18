import time
from datetime import datetime
import csv
import psycopg2
import pandas as pd
import logging

# logger = logging.getLogger(__name__)
#
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('../pythonProject/file.log')
#
# c_handler.setLevel(logging.INFO)
# f_handler.setLevel(logging.INFO)
#
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
#
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)

db_params = {
    "host": "localhost",
    "database": "baigiamasis",  #pakeisti
    "user": "postgres",
    "password": "riko789",
    "port": "5432"
}

# logger.info('Script started')
#
# def delete_table(conn_params):
#     connection = psycopg2.connect(**conn_params)
#     cursor = connection.cursor()
#     delete_query = """
#         DROP TABLE if EXISTS books
#     """
#     cursor.execute(delete_query)
#     print("Tables deleted successfuly")
#     connection.commit()
#     cursor.close()
#     connection.close()
#
# delete_table(db_params)

# def create_table(conn_params):
#     try:
#         connection = psycopg2.connect(**conn_params)
#         cursor = connection.cursor()
#         # logger.info('Connecting to the database...')
#
#         create_query1 = """
#             CREATE TABLE IF NOT EXISTS books2(
#                 book_id SERIAL PRIMARY KEY,
#                 author_name VARCHAR(255),
#                 author_last_name VARCHAR(255),
#                 book_title VARCHAR(255),
#                 publish_date DATE,
#                 ISBN VARCHAR(255),
#                 genre VARCHAR(255))
#         """

#         create_query2 = """
#             CREATE TABLE IF NOT EXISTS readers(
#                 reader_id SERIAL PRIMARY KEY,
#                 first_name VARCHAR(255),
#                 last_name VARCHAR(255),
#                 email VARCHAR(255),
#                 gender VARCHAR(255),
#                 birth_date DATE,
#                 category VARCHAR(255))
#         """
# #
#         create_query3 = """
#             CREATE TABLE IF NOT EXISTS orders(
#                 order_id SERIAL PRIMARY KEY,
#                 reader_id INTEGER REFERENCES readers(reader_id),
#                 book_id INTEGER REFERENCES books(book_id),
#                 date_taken DATE,
#                 date_returned DATE
#             )
#         """
#

        # cursor.execute(create_query1)
        # logger.info('Creating table books')
        # cursor.execute(create_query2)
        # # logger.info('Creating table readers')
        # cursor.execute(create_query3)
        # # logger.info('Creating table orders')
#
#         print("Tables created successfuly")
#
#         connection.commit()
#         cursor.close()
#         connection.close()
#     except Exception as e:
#         # logger.error("Failed to create tables", exc_info=True)
#         print(f"Error: {e}")
#
# create_table(db_params)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def insert_data_from_csv(conn_params, table_name, csv_file_path):
#     try:
#         connection = psycopg2.connect(**conn_params)
#         cursor = connection.cursor()
#
#         with open(csv_file_path, 'r') as file:
#             reader = csv.reader(file)
#             next(reader) #skip the header row
#             for row in reader:
#                 formatted_row = ', '.join([f"'{item}'" if not item.isdigit() else item for item in row])
#                 formatted_row = formatted_row.replace("'", "''")
#                 cursor.execute(f"INSERT INTO {table_name} VALUES ({formatted_row});")
#
#         connection.commit()
#         cursor.close()
#         connection.close()
#     except Exception as e:
#         print(f"Error: {e}")
#
#
# insert_data_from_csv(db_params, 'books', "C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/books_koreguotas.csv")
# insert_data_from_csv(db_params, 'readers', "C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/readers_koreguotas.csv")
#
# Connect to your database
# conn = psycopg2.connect(**db_params)

# # Create a cursor object
# cur = conn.cursor()
#
# # Execute the SQL command
# # cur.execute("ALTER TABLE orders ADD COLUMN order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP;")
# # cur.execute("ALTER TABLE readers ADD COLUMN username TEXT UNIQUE;")
# # cur.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")
# # cur.execute("ALTER TABLE readers ADD COLUMN password TEXT;")
#
#
# # Commit the changes and close the connection
# conn.commit()
# cur.close()
# conn.close()


# duomenys lentelems sukurti naudojant: https://www.mockaroo.com/