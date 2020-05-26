from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

from application import app, db
from application.auth.models import User
from application.auth.forms import Login, Registration, Edit, Password


bcrypt = Bcrypt(app)

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():

    if request.method == "GET":
        return render_template("auth/registration.html", form = Registration())

    form = Registration(request.form)
    if not form.validate():
            return render_template("auth/registration.html", form = form)

    username = User.query.filter_by(username=form.username.data).first()
    if username:
        return render_template("auth/registration.html", form = form,
                               error = "Käyttäjätunnus on jo käytössä")
    
    password = form.password.data
    hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')
    
    user = User(form.name.data, form.username.data, hashedPassword, form.info.data)
    db.session().add(user)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data, password=hashedPassword).first()
    login_user(user)

    return redirect(url_for("index"))  


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/login.html", form = Login())

    form = Login(request.form)
    if not form.validate():
            return render_template("auth/login.html", form = form)

    userFound = User.query.filter_by(username=form.username.data).first()
    if not userFound:
        return render_template("auth/login.html", form = form,
                               error = "Virheellinen käyttäjätunnus tai salasana")

    testPassword = form.password.data
    if not bcrypt.check_password_hash(userFound.password, testPassword):
        return render_template("auth/login.html", form = form,
                               error = "Virheellinen käyttäjätunnus tai salasana")

    login_user(userFound)

    return redirect(url_for("index"))  


@app.route("/auth/edit/", methods = ["GET", "POST"])
@login_required
def auth_edit():
   
    user = current_user
    
    if request.method == "POST":

        form = Edit(request.form) 
        if not form.validate():
            return render_template("auth/edit.html", form = form)

        if form.username.data != current_user.username:
            usernameFound = User.query.filter_by(username=form.username.data).first()
            if usernameFound:
                return render_template("auth/edit.html", form = form,
                               error = "Käyttäjätunnus on jo käytössä")

        user.name = form.name.data
        user.username = form.username.data
        user.info = form.info.data
        db.session().commit()
  
        return redirect(url_for("index"))

    return render_template("auth/edit.html", form = Edit(obj=user))

@app.route("/auth/changepassword", methods = ["GET", "POST"])
@login_required
def auth_changepassword():
    
    user = current_user
    
    if request.method == "POST":

        form = Password(request.form) 
        if not form.validate():
            return render_template("auth/password.html", form = form)

        user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session().commit()
  
        return redirect(url_for("auth_edit"))

    return render_template("auth/password.html", form = Password())

@app.route("/auth/delete")
@login_required
def auth_delete():
    
    user = current_user
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("index"))     
 

@app.route("/auth/logout")
@login_required
def auth_logout():
    
    logout_user()
    return redirect(url_for("index"))    
