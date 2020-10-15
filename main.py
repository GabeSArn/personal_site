from flask import Flask, request, render_template
from db import db_control as dbc
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

@app.route('/home')
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about_me_page():
    return render_template('about.html')

@app.route('/projects')
def preject_page():
    return render_template('projects.html')


if __name__=='__main__':
    app.run()
