import pymysql
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def add_project(json):
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="trakrApp",
        host="mysql-1935ce0b-bilalc8-2a11.j.aivencloud.com",
        password= os.getenv('MYSQL_PASSWORD'),
        read_timeout=timeout,
        port=15183,
        user="avnadmin",
        write_timeout=timeout,
    )

    try:
        cursor = connection.cursor()
        # SQL query to insert data into the `jobs` table
        sql = """
        INSERT INTO jobs (testType, client, entity, assignedTo)
        VALUES (%s, %s, %s, %s)
        """

        # Execute the query with the values from the JSON object
        cursor.execute(sql, (
            json["testType"],
            json["client"],
            json["entity"],
            json["assignedTo"]
        ))

        # Commit the transaction
        connection.commit()
    finally:
        connection.close()
