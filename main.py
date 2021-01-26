from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about_me_page():
    return render_template('about.html')

if __name__=='__main__':
    Port = int(os.environ.get('PORT', 17995))
    app.run(port=Port)
