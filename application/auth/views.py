from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registrationform.html", form = RegistrationForm())

    form = RegistrationForm(request.form)

    # validate here

    username = User.query.filter_by(username=form.username.data).first()

    if username:
        return render_template("auth/registrationform.html", form = form,
                               error = "Käyttäjätunnus on jo käytössä")
    
    user = User(form.name.data, form.username.data, form.password.data, form.info.data)

    db.session().add(user)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    login_user(user)
    return redirect(url_for("index"))  


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    # validate here

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Virheellinen käyttäjätunnus tai salasana")


    login_user(user)
    return redirect(url_for("index"))  



@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    
