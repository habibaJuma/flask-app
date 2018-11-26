from flask import Flask, render_template
from random import randint
import os

app = Flask(__name__)

@app.route('/')
def home():
        if not session.get('Sign in'):
                return render_template('signin.html')
        else:
                return "Correct" 

@app.route('/signin', method=['POST'])
def do_admin_login():
        if request.from['password'] == 'password' and request.from['Email'] == 'admin':session['sign_in'] = True
        else:
                flash('wrong password!')
        return home()

@app.route("/sign_out")
def signout():
        session['signed_in'] = False
        return home()

if __name__ == "__main__":
        app.secret_key = os.unrandom(12)
        app.run(debug=True,host='0.0.0.0', port=4000)


from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class SignupForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        print name, " ", email, " ", password
 
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()

