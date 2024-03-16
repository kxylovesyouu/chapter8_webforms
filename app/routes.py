from app import app
from flask import render_template, flash, redirect, url_for
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def index():
    
    
    """Index URL"""
    return render_template('shop.html', title='Shop Page')
    
@app.route('/about_me')
def about_me():
    
    
    """Index URL"""
    return render_template('about_me.html', title='About Me')
    
@app.route('/login', methods=['GET','POST'])
def login():
    
    
    """Index URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to log in {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login Page', form=form)


# 