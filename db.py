#!/usr/bin/python3

#Setup database for using djangoCRM

import os
import psycopg2

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCRM.settings')
    connector = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres"
    )

    cursor = connector.cursor()

    cursor.execute("CREATE DATABASE dcrm;")

except:
    print(f"Issue with database connection")