from flask import Flask, render_template, redirect, url_for, flash, jsonify, request
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from models import User, get_db_connection
from fetchJobs import fetch_all_jobs
from add_project import add_project
from del_project import del_project
from flask_wtf.csrf import CSRFProtect


login_manager = LoginManager()


def init_routes(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        print("Register route accessed")
        form = RegistrationForm()
        print("Form instantiated")

        if form.validate_on_submit():
            print("Form validated successfully")
            if form.password.data:
                hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
                print("hashed")
            else:
                flash('Password cannot be empty', 'danger')
                return redirect(url_for('register'))

            connection = get_db_connection()
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                               (form.username.data, form.email.data, hashed_password))
                connection.commit()
                print("posted")
            connection.close()
            flash('Your account has been created!', 'success')
            return redirect(url_for('login'))
        else:
            print("Form validation failed:", form.errors)

        return render_template('register.html', form=form)

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/')
    def home():
        jobs = fetch_all_jobs()
        return render_template('home.html', jobs=jobs)
    
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
    
        add_project(job_data)
    
        return jsonify({'status': 'success', 'message': 'Job added successfully!'})
    
    
    @app.route('/delete-job/<int:job_id>', methods=['DELETE'])
    def delete_job(job_id):
    
        del_project(job_id)
        return jsonify({'status': 'success', 'message': 'Job deleted successfully!'})
    