import pymysql
import os
from flask import Flask
from models import get_db_connection

def add_project(json):
    connection = get_db_connection()
    with connection.cursor() as cursor:
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
    
    connection.close()
