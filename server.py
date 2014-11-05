from flask import Flask, render_template
from flask.ext.misaka import Misaka
import os

app = Flask(__name__, static_url_path='')
Misaka(app)

@app.route('/')
@app.route('/index')
def index():
    posts = [
            {
                'title': 'how i learned to dong',
                'body': 'i used my donger'
                },
            ]

    posts = []
    for file in os.listdir("posts"):
        if not file.startswith('.') and file.endswith('.md'):
            with open(os.path.join("posts", file)) as opened_file:
                posts.append({
                    'title': os.path.splitext(file)[0],
                    'body': opened_file.read()
                    })

    return render_template('index.html',
                            posts=posts)

@app.route('/static/<filename>')
def css(filename):
    return app.send_static_file(filename)

app.run(debug=True)