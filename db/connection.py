import mysql.connector
from mysql.connector import Error

# You can load sensitive info from a .env file for security (optional)
# from dotenv import load_dotenv
# import os
# load_dotenv()

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="REMOTE_IP_ADDRESS",         # e.g., "192.168.1.100"
            user="your_username",
            password="your_password\",
            database="HostelSystem"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def test_connection():
    conn = get_connection()
    if conn:
        print("Database connection successful.")
        conn.close()
    else:
        print("Failed to connect to database.")
