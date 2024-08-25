from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

#job_data = {
#    'testType': test_type,
#    'client': client,
#    'entity': entity,
#    'assignedTo': assigned_to
#}

class ItemForm(FlaskForm):
    
    testType = StringField('testType', validators=[DataRequired()], render_kw={"class": "form-control"})
    
    client = StringField('client', validators=[DataRequired()], render_kw={"class": "form-control"})
    
    entity = StringField('entity', validators=[DataRequired()], render_kw={"class": "form-control"})
    
    assignedTo = StringField('assignedTo', validators=[DataRequired()], render_kw={"class": "form-control"})
    

