import pymysql
import os
from flask import Flask
from models import get_db_connection

def fetch_all_jobs():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs")
        results = cursor.fetchall()
    connection.close()
    #print(results)
    jobs = [] 
    for row in results:
        jobs.append(dict(row))
    #print("jobs result",jobs)    
    jobs.reverse()
    return jobs
    
