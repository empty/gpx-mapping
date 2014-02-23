
import glob
import os

from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['gpx'])
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(PROJECT_DIR, './static/gpx')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    os.chdir(UPLOAD_FOLDER)
    files = glob.glob('*.gpx')
    return render_template('index.html', files=files)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload_file.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
