import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connectToDB(isLocal=True):
    try:
        if isLocal:
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password=os.getenv("DB_PASSWORD"),
                dbname="postgres",  # update to your DB name
                port=5432
            )
        else:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                dbname=os.getenv("DB_NAME"),
                port=os.getenv("DB_PORT")
            )
        return conn
    except Exception as e:
        print("Connection failed:", e)
        return None


def retrieveData(db_connection):
    try:
        cur = db_connection.cursor()
        cur.execute("SELECT x, y FROM coordinates")
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        print("Error retrieving data:", e)
        return []
