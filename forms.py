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
                         render_kw={
                             "class": "form-control",
                             "id": "clientName"
                         })


class TestForm(FlaskForm):
    test = StringField('Test',
                       validators=[DataRequired()],
                       render_kw={
                           "class": "form-control",
                           "id": "testName"
                       })


class JobForm(FlaskForm):
    job = StringField('Job',
                      validators=[DataRequired()],
                      render_kw={
                          "class": "form-control",
                          "id": "jobName"
                      })


class TaskForm(FlaskForm):
    task = StringField('Task',
                       validators=[DataRequired()],
                       render_kw={
                           "class": "form-control",
                           "id": "taskName"
                       })
