from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__)

    # a simple response that says hello
    @app.route('/')
    @app.route('/jobs')
    def jobs():
        return render_template('index.html')

    return app

