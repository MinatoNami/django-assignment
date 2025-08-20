import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def connectToDB(isLocal=True):
    try:
        if (isLocal):
            # Connect to local PostgreSQL
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",)
        else:
            # Connect to AWS RDS
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT")
            )
        return conn

    except Exception as e:
        print("Connection failed:", e)


def testDBConnection(db_connection):
    try:
        cur = db_connection.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print("Connected! PostgreSQL version:", db_version)
        cur.close()
        return True
    except Exception as e:
        print("Error testing database connection:", e)
        return False


def retrieveData(db_connection):
    try:
        cur = db_connection.cursor()
        cur.execute("SELECT x, y FROM coordinates")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except Exception as e:
        print("Error retrieving data:", e)

# Used to delete table


def deleteTable(db_connection):
    try:
        cur = db_connection.cursor()
        cur.execute("DROP TABLE IF EXISTS coordinates")
        cur.close()
    except Exception as e:
        print("Error deleting table:", e)


# isLocal=True for local db testing
db_connection = connectToDB(isLocal=True)
db_connected = testDBConnection(db_connection)

# Adding table and data into DB
# if db_connected and db_connection:
#     print("Database connection is active.")
#     # db_connection.autocommit = True
#     cur = db_connection.cursor()

#     # Create table with x, y columns
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS coordinates (
#             id SERIAL PRIMARY KEY,
#             x DOUBLE PRECISION,
#             y DOUBLE PRECISION
#         )
#     """)
#     cur.execute("INSERT INTO coordinates (x, y) VALUES (%s, %s)", (10, 20))
#     cur.execute("INSERT INTO coordinates (x, y) VALUES (%s, %s)", (15.5, -3.2))
#     print("Table created and data inserted successfully.")
#     cur.close()
#     db_connection.commit()
#     db_connection.close()

# else:
#     print("Database connection failed.")

# Testing data retrieval
retrieveData(db_connection)
