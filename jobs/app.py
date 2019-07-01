from flask import (
    Flask,
    g,
    render_template,
    flash,
    redirect,
    url_for,
    abort
)

app = Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
