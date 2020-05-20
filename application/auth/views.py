from flask import render_template, request, redirect, url_for

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm

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


    print("Käyttäjä " + user.name + " löytyi")
    return redirect(url_for("index"))  
