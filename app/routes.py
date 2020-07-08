from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Marcin'}
    posts = [
        {
            'author' : {'username':'Jan'},
            'body'   : 'Beautiful day in Cracow!'
        },
        {
            'author' : {'username':'Anna'},
            'body'   : 'Jojorabit is great movie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)