from flask import Flask, render_template, redirect, url_for, flash
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from wtform_fields import *
from models import *

# configure app
app = Flask(__name__)
app.secret_key = 'Illuminati'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://wgprfdrnwgbedc:b055adf6e59127a38964e1b28e69998db0a1c9bd5e126b8de7052551cd5e85bc@ec2-18-214-211-47.compute-1.amazonaws.com:5432/dde4krt7hro8q5"
db = SQLAlchemy(app)

# configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):

    return User.query.get(int(id))

@app.route("/", methods=['GET', 'POST'])
def index():

    # to avoid user to access signup page after being logged in
    if current_user.is_authenticated:
        return redirect(url_for('chat'))

    reg_form = RegistrationForm()

    # updated database if validation success
    if reg_form.validate_on_submit():

        # extract form data
        username = reg_form.username.data
        password = reg_form.password.data

        # generate hash using pbkdf2
        # we can also salt and number of iterations for password hashing using syntax: 
        # pbkdf2_sha256.using(rounds=1000, salt_size=8).hash(password)
        hashed_password = pbkdf2_sha256.hash(password)
        
        # add user to database
        user = User(username = username, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Regestired successfully. Please Login!!', category='success')

        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    # to avoid user to access login page after being logged in
    if current_user.is_authenticated:
        return redirect(url_for('chat'))

    login_form = LoginForm()

    # Allow login if validation is successful
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    # else return back to login page with validation errors
    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET', 'POST'])
# @login_required
def chat():

    if not current_user.is_authenticated:
        flash('Please login!', category='danger')
        return redirect(url_for('login'))

    return "Chat with me ;)"

@app.route("/logout", methods=['GET'])
def logout():

    # to avoid user to access logout functationality without being logged in
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    logout_user()
    flash("You have logged out successfully!", category='success')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)