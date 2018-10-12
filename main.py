from flask import Flask, request, redirect, render_template
import cgi
import os
   
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
   return render_template('form.html')

@app.route("/validate", methods=['POST'])
def analyze_text():
    username = request.form['username']
    password = request.form['password']
    ver_password = request.form['ver_password']

    username_error = ''
    password_error = ''
    notmatch_error = ''

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Not a valid username'
        username = ''
    
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Not a valid password'

    if  ver_password != password:
        notmatch_error = 'Passwords must match'

    if not username_error or not password_error or not notmatch_error:
        return redirect('/welcome?username={}'.format(username))

    else:
        return render_template('form.html', username_error=username_error, password_error=password_error, notmatch_error=notmatch_error,username=username)

@app.route("/welcome" , methods=['GET','POST'] )
def welcome_message():
    username = request.args.get('username')
    return render_template('welcome_greeting.html', username =
    username)


app.run()   