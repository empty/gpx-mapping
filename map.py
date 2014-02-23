
import glob
import os

from flask import Flask, render_template

app = Flask(__name__)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    os.chdir(os.path.join(PROJECT_DIR, "./static/gpx"))
    files = glob.glob("*.gpx")
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run()
