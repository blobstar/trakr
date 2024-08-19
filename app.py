from re import DEBUG
from flask import Flask, render_template
import pymysql
from fetchJobs import fetch_all_jobs

app = Flask(__name__)

#adding a fake db


#def load_jobs_fromd_db():
#  with cursor.connect() as conn:
 #   result = conn.execute("SELECT * FROM jobs")
  #  jobs = [] 
   # for row in result.all():
    #  jobs.append(dict(row))
    #return jobs




  
@app.route('/')
def hello_world():
    jobs = fetch_all_jobs();
    print(fetch_all_jobs())
    return render_template('home.html',jobs=jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)