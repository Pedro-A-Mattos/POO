from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators, ValidationError
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from ..admin import models


class CustomerRegisterForm(FlaskForm):
    name = StringField('Nome: ', [validators.DataRequired()])
    username = StringField('Sobrenome: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Senha: ', [validators.DataRequired()])
    confirm = PasswordField('Repetir senha: ', [validators.DataRequired(), validators.EqualTo('password', message=' Both password must match! ')])
    profile = FileField('Profile', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Image only please')])
    country = StringField('Estado: ', [validators.DataRequired()])
    city = StringField('Cidade: ', [validators.DataRequired()])
    contact = StringField('Contato: ', [validators.DataRequired()])
    address = StringField('Endereço: ', [validators.DataRequired()])
    zipcode = StringField('Cep: ', [validators.DataRequired()])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        if models.User.query.filter_by(username=username.data).first():
            raise ValidationError("Este nome de usuário já está em uso!")

    def validate_email(self, email):
        if models.User.query.filter_by(email=email.data).first():
            raise ValidationError("Este endereço de e-mail já está em uso")


class CustomerLoginForm(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Senha: ', [validators.DataRequired()])
