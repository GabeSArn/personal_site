from flask import Flask, request, render_template
from forms import ContactForm
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about_me_page():
    # form = ContractForm()
    #
    # if request.method == 'POST':
    #     return 'Form Submitted.'
    # elif request.method == 'GET':
    return render_template('about.html', form=form)

if __name__=='__main__':
    Port = int(os.environ.get('PORT', 17995))
    app.run(port=Port)
