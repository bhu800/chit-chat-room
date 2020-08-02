from flask import Flask, render_template

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
    if reg_form.validate_on_submit():

        # extract form data
        username = reg_form.username.data
        password = reg_form.password.data
 
        # Check if username already exists
        # user_object = User.query.filter_by(username = username).first()
        # if user_object:
        #     return "Oops! Someone else has already taken that username."
        
        # add user to database
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into db!"


    return render_template("index.html", form=reg_form)

if __name__ == "__main__":
    app.run(debug=True)