from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired


class Menu(FlaskForm):
    menu_choices = [('registration', 'Registration'), ('aesk', 'AESK'),
     ('sk_update', 'Update Session Key'), ('password_altered', 'Update Password')]
    menu = RadioField('Menu', choices=menu_choices)
    submit = SubmitField('Proceed')  


class Registration(FlaskForm):

    IDmu = StringField('ID', validators=[DataRequired()])
    PWmu = StringField('Password', validators=[DataRequired()])
    s = StringField('Random Number', validators=[DataRequired()])
    submit = SubmitField('Register')


class AESK(FlaskForm):

    PW1mu = StringField('ID', validators=[DataRequired()])
    snew = StringField('Random Number 1', validators=[DataRequired()])    
    Nm = StringField('Random Number 2', validators=[DataRequired()])
    Nf = StringField('Random Number for FA', validators=[DataRequired()])
    Nf2 = StringField('Random Number 2 for FA', validators=[DataRequired()])
    submit = SubmitField('Proceed')


class SK_Update(FlaskForm):

    Nstarm = StringField('New Random Number', validators=[DataRequired()])
    Nstarf = StringField('New Random Number for FA', validators=[DataRequired()])    
    Kmf = StringField('New Session Key', validators=[DataRequired()])
    submit = SubmitField('Update Session Key')


class Password_Altered(FlaskForm):

    IDmu = StringField('ID', validators=[DataRequired()])
    PWmu = StringField('Password', validators=[DataRequired()])    
    PWmu_new = StringField('New Password', validators=[DataRequired()])
    submit = SubmitField('Change Password')
