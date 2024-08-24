from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddJobForm(FlaskForm):
    test_type = StringField('Test Type', validators=[DataRequired()])
    client = StringField('Client', validators=[DataRequired()])
    entity = StringField('Entity', validators=[DataRequired()])
    assigned_to = StringField('Assigned To', validators=[DataRequired()])
    submit = SubmitField('Submit')