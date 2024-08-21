import pymysql
import os
from flask import Flask
from models import get_db_connection

def del_project(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        # SQL query to insert data into the `jobs` table
        sql = "DELETE FROM jobs WHERE id = %s"
        cursor.execute(sql, (id))
        connection.commit()
    connection.close()
