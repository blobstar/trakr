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
    testType = StringField('Test Type', 
                           validators=[DataRequired()], 
                           render_kw={"class": "form-control", "id": "testType"})

    client = StringField('Client', 
                         validators=[DataRequired()], 
                         render_kw={"class": "form-control", "id": "client"})

    entity = StringField('Entity', 
                         validators=[DataRequired()], 
                         render_kw={"class": "form-control", "id": "entity"})

    assignedTo = StringField('Assigned To', 
                             validators=[DataRequired()], 
                             render_kw={"class": "form-control", "id": "assignedTo"})
    

