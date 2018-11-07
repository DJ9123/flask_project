from flask import Flask, render_template, abort, request, url_for, redirect, flash
from flask_login import LoginManager, current_user, login_user, logout_user

from models.user import User

# app = Flask(__name__)
app = Flask("myapp")
app.secret_key = "askjdnaksjndbakjsn"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

sample_user = {
    "name": "user",
    "email": "user@email.com",
    "password": "password"
}

@login_manager.user_loader
def load_user(email):
    # example using a DB
    # sample_user = db.get_user("email")
    if (email == sample_user["email"]):
        return User(sample_user["name"], sample_user["email"])
    return None

@app.route("/")
def index():
    return render_template("index.html") # not the file path but the name of the file inside of the template folder


@app.route("/login", methods=["GET", "POST", "PUT", "UPDATE", "DELETE"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if password == sample_user["password"]:
            user = User(sample_user["name"], sample_user["email"])
            login_user(user)
            return redirect(url_for("index"))
        flash("Incorrect password...")
        return redirect(url_for("login"))
        # print(dict(request.form))
        # print(dict(request.form)["email"])
        # print(dict(request.form)["password"])
    return render_template("login.html")

@app.route("/register")
def register():
    return "This is the register page"

@app.route("/logout")
def logout():
    return "This is the logout page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)