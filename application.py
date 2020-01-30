from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


application = Flask(__name__)
Bootstrap(application)


@application.route('/')
@application.route('/index.html')
def home():
    TITLE = 'Object detection'
    return render_template('index.html', TITLE=TITLE)


if __name__ == '__main__':
    application.run(debug=True)
