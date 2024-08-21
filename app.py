from re import DEBUG
from flask import Flask, render_template, request, jsonify
import pymysql
from fetchJobs import fetch_all_jobs
from add_project import add_project
from del_project import del_project

sqlPass = ""

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
    #print(fetch_all_jobs())
    return render_template('home.html',jobs=jobs)

@app.route('/submit-job', methods=['POST'])
def submit_job():
    test_type = request.form['testType']
    client = request.form['client']
    entity = request.form['entity']
    assigned_to = request.form['assignedTo']

    job_data = {
        'testType': test_type,
        'client': client,
        'entity': entity,
        'assignedTo': assigned_to
    }

    # Save the data to the database (add your logic here)
    #print(f"Test Type: {test_type}, Client: {client}, Entity: {entity}, Assigned To: {assigned_to}")
    add_project(job_data)
    # Return a JSON response
    return jsonify({'status': 'success', 'message': 'Job added successfully!'})


@app.route('/delete-job/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    # Implement your deletion logic here using the job_id
    del_project(job_id)
    return jsonify({'status': 'success', 'message': 'Job deleted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)