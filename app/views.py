from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'beautiful day in portland!'
        },
        {
            'author': {'nickname': 'susano'},
            'body': 'The Avengers was great...'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
