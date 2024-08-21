import pymysql
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def del_project(id):
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
        sql = "DELETE FROM jobs WHERE id = %s"
        cursor.execute(sql, (id))
        connection.commit()

    finally:
        connection.close()
