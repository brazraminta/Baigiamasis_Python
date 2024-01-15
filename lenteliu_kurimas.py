import time
from datetime import datetime
import psycopg2
import pandas as pd
import logging

logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('../pythonProject/file.log')

c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

db_params = {
    "host": "localhost",
    "database": "baigiamasis",  #pakeisti
    "user": "postgres",
    "password": "riko789",
    "port": "5432"
}

logger.info('Script started')

def delete_table(conn_params):
    connection = psycopg2.connect(**conn_params)
    cursor = connection.cursor()
    delete_query = """
        DROP TABLE if EXISTS books, readers
    """
    cursor.execute(delete_query)
    print("Tables deleted successfuly")
    connection.commit()
    cursor.close()
    connection.close()

def create_table(conn_params):
    try:
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        logger.info('Connecting to the database...')

        create_query1 = """
            CREATE TABLE IF NOT EXISTS books(
                id SERIAL PRIMARY KEY,
                author_name VARCHAR(255),
                author_last_name VARCHAR(255),
                book_title VARCHAR(255),
                publish_date DATE,
                ISBN VARCHAR(255),
                genre VARCHAR(255))
        """


        create_query2 = """
            CREATE TABLE IF NOT EXISTS readers(
                id VARCHAR(255),
                reader_name VARCHAR(255),
                reader_last_name VARCHAR(255),
                reader_category VARCHAR(255),
                birth_date DATE,
                reader_email VARCHAR(255),
                gender VARCHAR(255))
        """

        cursor.execute(create_query1)
        logger.info('Creating table books')
        cursor.execute(create_query2)
        logger.info('Creating table readers')
        print("Tables created successfuly")

        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        logger.error("Failed to create tables", exc_info=True)

create_table(db_params)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def insert_data(all_books, readers, conn_params):
#     connection = psycopg2.connect(**conn_params)
#     cursor = connection.cursor()
#
#     insert_query1 = """
#         INSERT INTO books (
#         author_name,
#         author_last_name,
#         book_title,
#         publish_date,
#         ISBN,
#         genre) VALUES (%s, %s, %s, %s, %s, %s)
#         """
#     for file in all_books:
#         # Read the CSV file using pandas
#         df = pd.read_csv(file)
#
#         # Convert the 'publish_date' column to the datetime format
#         df['publish_date'] = pd.to_datetime(df['publish_date'])
#
#
#         # Loop over the rows in the DataFrame
#         for index, row in df.iterrows():
#             author_name = row['author_name']
#             author_last_name = row['author_last_name']
#             book_title = row['book_title']
#             publish_date = row['publish_date'].strftime('%Y-%m-%d')
#             ISBN = row['ISBN']
#             genre = row['genre']
#
#         cursor.execute(insert_query1, (author_name, author_last_name, book_title, publish_date, ISBN, genre))
#
#     insert_query2 = f"""
#         INSERT INTO readers (
#         reader_name,
#         reader_last_name,
#         reader_category,
#         birth_date,
#         reader_email,
#         gender) VALUES (%s, %s, %s, %s)
#     """
#     for reader in readers:
#         reader_name = reader['reader_name']
#         reader_last_name = reader['reader_last_name']
#         reader_category = reader['reader_category']
#         birth_date = reader['birth_date']
#         reader_email = reader['reader_email']
#         gender = reader['gender']
#
#         cursor.execute(insert_query2, (reader_name, reader_last_name, reader_category, birth_date, reader_email, gender))
#
#     print("Data for 'books' and 'readers' inserted successfuly")
#
#     cursor.execute("SELECT * FROM books LIMIT 5")
#     logger.info("First few rows from 'books':")
#     print(cursor.fetchall())
#
#     cursor.execute("SELECT * FROM readers LIMIT 5")
#     logger.info("First few rows from 'readers':")
#     print(cursor.fetchall())
#
#     connection.commit()
#     cursor.close()
#     connection.close()
#
# # List of CSV files
# all_books = ["C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/MOCK_DATA_books1.csv",
#          "C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/MOCK_DATA(1)_books2.csv",
#          "C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/MOCK_DATA(2)_books3.csv"]
# readers = "C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/MOCK_DATA(3)_readers.csv"
#
# insert_data(all_books, readers, db_params)