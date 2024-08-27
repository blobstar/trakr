from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

#job_data = {
#    'testType': test_type,
#    'client': client,
#    'entity': entity,
#    'assignedTo': assigned_to
#}

class ClientForm(FlaskForm):
    client = StringField('Client', 
                         validators=[DataRequired()], 
                         render_kw={"class": "form-control", "id": "client-name"})

class TestForm(FlaskForm):
    client = StringField('Test', 
                         validators=[DataRequired()], 
                         render_kw={"class": "form-control", "id": "test-name"})

class JobForm(FlaskForm):
    client = StringField('Job', 
                         validators=[DataRequired()], 
                         render_kw={"class": "form-control", "id": "job-name"})

class TaskForm(FlaskForm):
    client = StringField('Task', 
                         validators=[DataRequired()], 
                         render_kw={"class": "form-control", "id": "task-name"})
    

