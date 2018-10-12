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
    email =  request.form['email']

    username_error = ''
    password_error = ''
    notmatch_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Not a valid username'
        username = ''
    
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Not a valid password'

    if  ver_password != password:
        notmatch_error = 'Passwords must match'

    if email != '' and len(email) < 3 or email != '' and len(email) > 20 or email != '' and "@" and "." not in email:
        email_error = "That's not a valid email"
        email = ''


    if username_error or password_error or notmatch_error or email_error:
        return render_template('form.html', username_error=username_error, password_error=password_error, 
        notmatch_error=notmatch_error, email_error=email_error, username=username, email=email)
        
    else:
        return redirect('/welcome?username={}'.format(username))

@app.route("/welcome" , methods=['GET','POST'] )
def welcome_message():
    username = request.args.get('username')
    return render_template('welcome_greeting.html', username =
    username)


app.run()   