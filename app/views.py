from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

# index view function suppressed for brevity

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me' + str(form.remember_me.data))
        return redirect('/index')
    return render_template("login.html", title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])


@app.route("/index")
def index():
    #fake user
    user = {'nickname': 'yanzhi'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", user = user, posts = posts)
