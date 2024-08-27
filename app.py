from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, make_response
from flask_wtf import CSRFProtect
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFError
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired
import pymysql.cursors
from dotenv import load_dotenv
import os
from forms import ClientForm

#test
#test2





load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Replace with a strong secret key

@app.after_request
def set_csp(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
        "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
        "img-src 'self' data:;"
    )
    return response

# Configure MySQL
app.config['MYSQL_HOST'] = 'mysql-1935ce0b-bilalc8-2a11.j.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'trakrApp'
app.config['MYSQL_PORT'] = 15183

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize MySQL connection
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT'],  # Port number specified here
        cursorclass=pymysql.cursors.DictCursor
    )

# CREATE
@app.route('/items', methods=['POST'])
#@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def create_item():
    print("route success")
    form = ClientForm(request.form)
    if form.validate():
        testType = form.testType.data
        client = form.client.data
        entity = form.entity.data
        assignedTo = form.assignedTo.data

        connection = get_db_connection()
        with connection.cursor() as cursor:
            print("con")
            cursor.execute('INSERT INTO jobs (testType, client, entity, assignedTo) VALUES (%s, %s, %s, %s)', (testType, client,entity,assignedTo))
            connection.commit()
        connection.close()

        flash('Your job has been created!', 'success')
        return redirect(url_for('home'))
    return jsonify({'message': 'Invalid data'}), 400

# Read
@app.route('/', methods=['GET'])
def home():
    form = ClientForm()
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM jobs')
        items = cursor.fetchall()
    connection.close()
    jobs = [] 
    for row in items:
        jobs.append(dict(row))
    print("jobs result",jobs)    
    jobs.reverse()

    return render_template('home.html', jobs=jobs, form=form)

# Update
@app.route('/update-job/<int:id>', methods=['POST'])
@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def update_item(id):
    print("in update route")
    # Ensure the request is JSON
    form = ClientForm(request.form)
    print(form.testType.data)
    if form.validate():
        testType = form.testType.data
        client = form.client.data
        entity = form.entity.data
        assignedTo = form.assignedTo.data
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute('UPDATE jobs SET testType = %s, client = %s, entity = %s, assignedTo = %s WHERE id = %s',(testType, client, entity, assignedTo, id))
        connection.commit()
        connection.close()
        return redirect(url_for('home'))
    return jsonify({'status':'catastrophe'})
    


# Delete
@app.route('/delete-job/<int:id>', methods=['DELETE'])
@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def delete_item(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM jobs WHERE id = %s', (id,))
        connection.commit()
    connection.close()

    return jsonify({'status': 'success', 'message': 'Item deleted successfully'})

# Error handling
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify({'message': 'CSRF token missing or incorrect'}), 400

# get a specific job
@app.route('/get-job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    # Fetch job data from the database
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT testType, client, entity, assignedTo FROM jobs WHERE id = %s', (job_id,))
        job = cursor.fetchone()

    if not job:
        return jsonify({'message': 'Job not found'}), 404

    # Convert fetched data into a dictionary
    job_data = {
        'testType': job['testType'],
        'client': job['client'],
        'entity': job['entity'],
        'assignedTo': job['assignedTo']
    }

    # Initialize the form with the job data
    ClientForm(data=job_data)

    return jsonify({'status': 'success', 'message': 'Found the Job!', 'testType': job['testType'], 'client': job['client'], 'entity': job['entity'], 'assignedTo': job['assignedTo']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
