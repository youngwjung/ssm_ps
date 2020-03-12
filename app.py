import mysql.connector
import os

from env import *

try:
    db = mysql.connector.connect(
        host = os.environ['DB_URL'],
        user = os.environ['DB_USER'],
        passwd = os.environ['DB_PASSWORD'],
        connection_timeout = 5
    )
    print (f"Connected to {os.environ['DB_URL']}")
except Exception as e: print(e)