import pymysql
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def fetch_all_jobs():
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
        # Insert data (uncomment if needed)
        #cursor.execute("""
         #    INSERT INTO jobs (testType, client, entity, assignedTo) 
          #   VALUES ('Accounting Records', 'TestClient1', 'Entity1','Someone')
        #""")
        #connection.commit()
        cursor.execute("SELECT * FROM jobs")
        results = cursor.fetchall()
        #print(results)
        jobs = [] 
        for row in results:
            jobs.append(dict(row))
        #print("jobs result",jobs)    
        jobs.reverse()
        return jobs
    finally:
        connection.close()
