from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
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
    test = SelectField('Test',
                       choices=[("Employee Costs", "Employee Costs"),
                                ("Accounting Records", "Accounting Records"),
                                ("Property Plant and Equipment", "Property Plant and Equipment"),
                                ("SAP to Kronos","SAP to Kronos"),
                                ("Prelim AR's","Prelim AR's")
                                ],
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
