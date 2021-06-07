from wtforms import BooleanField, StringField, PasswordField, validators, ValidationError
from flask_wtf import FlaskForm, Form
from .models import User


class RegistrationForm(FlaskForm):
    name = StringField('Nome', [validators.Length(min=4, max=25)])
    username = StringField('Sobrenome', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('Confirme a sua senha', message='As senhas devem ser iguais')
    ])
    PasswordField('Repita a sua senha')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nome de usuário já em uso.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email já cadastrado para outro usuário')


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [validators.DataRequired()])
