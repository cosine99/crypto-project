from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired


class Menu(FlaskForm):
    menu_choices = [('registration', 'Registration'), ('aesk', 'AESK'),
     ('sk_update', 'Update Session Key'), ('password_altered', 'Update Password')]
    menu = RadioField('Menu', choices=menu_choices)
    submit = SubmitField('Proceed')  


class Registration(FlaskForm):

    IDmu = StringField('ID (IDmu)', validators=[DataRequired()])
    PWmu = PasswordField('Password (PWmu)', validators=[DataRequired()])
    s = StringField('Random Number (s)', validators=[DataRequired()])
    submit = SubmitField('Register')


class AESK(FlaskForm):

    IDmu = StringField('ID (IDmu)', validators=[DataRequired()])
    PW1mu = PasswordField('Password (PW1mu)', validators=[DataRequired()])
    snew = StringField('Random Number (snew)', validators=[DataRequired()])    
    Nm = StringField('Random Number 2(Nm)', validators=[DataRequired()])
    Nf = StringField('Random Number for FA(Nf)', validators=[DataRequired()])
    Nf2 = StringField('Random Number 2 for FA(Nf2)', validators=[DataRequired()])
    submit = SubmitField('Proceed')


class SK_Update(FlaskForm):

    Nstarm = StringField('New Random Number (N*m)', validators=[DataRequired()])
    Nstarf = StringField('New Random Number for FA(N*f)', validators=[DataRequired()])    
    Kmf = StringField('New Session Key (Kmf)', validators=[DataRequired()])
    submit = SubmitField('Update Session Key')


class Password_Altered(FlaskForm):

    IDmu = StringField('ID (IDmu)', validators=[DataRequired()])
    PWmu = PasswordField('Password (PWmu)', validators=[DataRequired()])    
    PWmu_new = PasswordField('New Password(PWmu_new)', validators=[DataRequired()])
    submit = SubmitField('Change Password')
