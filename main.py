from flask import Flask, request, render_template
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

@app.route('/home')
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about_me_page():
    return render_template('about.html')

if __name__=='__main__':
    app.run()
