from flask import Flask, render_template, redirect, url_for

from wtform_fields import *
from models import *

app = Flask(__name__)
app.secret_key = 'Illuminati'

# Configure app
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://wgprfdrnwgbedc:b055adf6e59127a38964e1b28e69998db0a1c9bd5e126b8de7052551cd5e85bc@ec2-18-214-211-47.compute-1.amazonaws.com:5432/dde4krt7hro8q5"
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # updated database if validation success
    if reg_form.validate_on_submit():

        # extract form data
        username = reg_form.username.data
        password = reg_form.password.data
        
        # add user to database
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        return "Logged in, successfully!"

    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)