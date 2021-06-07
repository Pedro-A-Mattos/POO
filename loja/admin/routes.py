from flask import render_template, session, request, redirect, url_for, flash
from loja import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from loja.produto.models import Addproduct
import os


@app.route('/admin')
def admin():
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin page', products=products)




@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        flash(f'Bem vindo {form.name.data} Obrigado por se registrar', 'success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/register.html', title='Register user', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Bem vindo {form.email.data} você está logado agora', 'success')
            return redirect(url_for('admin'))
        else:
            flash(f'Email ou senha inválidos', 'success')
            return redirect(url_for('login'))
    return render_template('admin/login.html', title='Login page', form=form)
