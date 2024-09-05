from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, make_response
from flask_wtf import CSRFProtect
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFError
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired
import pymysql.cursors
from dotenv import load_dotenv
import os
from forms import ClientForm, TestForm, JobForm, TaskForm

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
@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def create_item():
    print("route success")
    form = ClientForm(request.form)
    if form.validate():
        client = form.client.data

        connection = get_db_connection()
        with connection.cursor() as cursor:
            print("con")
            cursor.execute('INSERT INTO clients (name) VALUES (%s)', (client))
            connection.commit()
        connection.close()

        flash('Your client has been created!', 'success')
        return jsonify({'status': 'success', 'message': 'Client created successfully'}), 200
    return jsonify({'message': 'Invalid data'}), 400

# Read home
@app.route('/', methods=['GET'])
def home():
    form = ClientForm()
    connection = get_db_connection()
    try: #get all clients
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM clients')
            items = cursor.fetchall()
        clients = [] 
        for row in items:
            clients.append(dict(row)) 
        clients.reverse()
        # get all tests
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM tests')
            test = cursor.fetchall()
        tests = [] 
        for row in test:
            tests.append(dict(row)) 
        tests.reverse()
        print(tests)

    finally:
        connection.close()

    return render_template('homeClients.html', clients=clients, form=form,tests=tests)

# Read projects
@app.route('/Projects', methods=['GET'])
def projectHome():
    form = ClientForm()
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM tests')
        items = cursor.fetchall()
    connection.close()
    tests = [] 
    for row in items:
        tests.append(dict(row))  
    tests.reverse()
    

    return render_template('home.html', tests=tests, form=form)

# Update
@app.route('/update-client/<int:id>', methods=['POST'])
#@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def update_item(id):
    #print("in update route")
    # Ensure the request is JSON
    form = ClientForm(request.form)
    #print(form.testType.data)
    if form.validate():
        client = form.client.data
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute('UPDATE clients SET name = %s WHERE id = %s',(client, id))
            connection.commit()
        connection.close()
        return jsonify({'status': 'success', 'message': 'Client created successfu'}), 200
    return jsonify({'status':'catastrophe'})
    


# Delete
@app.route('/delete-client/<int:id>', methods=['DELETE'])
@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def delete_item(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM clients WHERE id = %s', (id,))
        connection.commit()
    connection.close()

    return jsonify({'status': 'success', 'message': 'Item deleted successfully'})

# Error handling for CSRF
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify({'message': 'CSRF token missing or incorrect'}), 400

# get a specific client
@app.route('/get-client/<int:client_id>', methods=['GET'])
def get_client(client_id):
    # Fetch client data from the database
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT name FROM clients WHERE id = %s', (client_id,))
        client = cursor.fetchone()

    if not client:
        return jsonify({'message': 'Client not found'}), 404

    # Convert fetched data into a dictionary
    client_data = {
        'client': client['name']
    }

    # Initialize the form with the client data
    ClientForm(data=client_data)

    return jsonify({'status': 'success', 'message': 'Found the Client!', 'client': client['name']})

@app.route('/client/<int:client_id>/tests')
def view_client_tests(client_id):
    form = TestForm(request.form)
    connection = get_db_connection()
    try:
        # Get the specific tests for that client ID
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM tests WHERE clientID = %s', (client_id,))
            items = cursor.fetchall()
            tests = [] 
            for row in items:
                tests.append(dict(row)) 
            tests.reverse()

        # Get the client name
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM clients WHERE id = %s', (client_id,))
            client_name_result = cursor.fetchone()
        clientName = client_name_result['name'] if client_name_result else 'Unknown Client'

    finally:
        connection.close()

    return render_template('client_tests.html', client_id=client_id, test=tests, clientName=clientName, form=form, client=client_id)


@app.route('/createTestInClient/<int:client_id>', methods=['POST'])
@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def createTestInClient(client_id):
    form = TestForm(request.form)
    if form.validate():
        test = form.test.data
        print("form valid")
        connection = get_db_connection()
        with connection.cursor() as cursor:
            print("connected to sql")
            cursor.execute('INSERT INTO tests (ClientID, name) VALUES (%s, %s)', (client_id, test))
            connection.commit()
        connection.close()

        flash('Your client has been created!', 'success')
        return jsonify({'status': 'success', 'message': 'Client created successfully'}), 200
    return jsonify({'message': 'Invalid data'}), 400

# Delete
@app.route('/delete-test/<int:id>', methods=['DELETE'])
@csrf.exempt  # Temporarily exempting from CSRF to simplify testing
def delete_test(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM tests WHERE id = %s', (id,))
        connection.commit()
    connection.close()

    return jsonify({'status': 'success', 'message': 'Test deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
