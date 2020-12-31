from flask import Flask, request, render_template
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
    Port = int(os.environ.get('PORT', 17995))
    my_app.run(debug = True, port=Port)
