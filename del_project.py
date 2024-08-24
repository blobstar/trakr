import pymysql
import os
from flask import Flask
from models import get_db_connection

def del_project(id):
    print("got connections1")
    connection = get_db_connection()
    print("got connections2")
    with connection.cursor() as cursor:
        print("got connections3")
        # SQL query to insert data into the `jobs` table
        sql = "DELETE FROM jobs WHERE id = %s"
        cursor.execute(sql, (id))
        connection.commit()
    connection.close()
