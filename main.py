from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)    

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()



@app.route("/submitted" , methods=["POST"])
def submitted():
    username = request.form["username"]
    template = jinja_env.get_template('welcome_greeting.html')
    return template.render(username =
    username)

#return redirect('/submitted?username={0}'.format(username))

app.run()   