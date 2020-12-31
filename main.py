from flask import Flask, request, render_template
import waitress
import os
my_app = Flask(__name__)

@my_app.route('/home')
@my_app.route('/')
def hello_world():
    return render_template('home.html')

@my_app.route('/about')
def about_me_page():
    return render_template('about.html')

if __name__=='__main__':
    my_app.debug = True
    waitress.serve(my_app, port=int(os.environ.get('PORT', 17995)))
