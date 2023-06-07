"""
A server file for a CSV to JSON converter
"""
from flask import Flask, render_template, redirect, request, url_for, flash, send_from_directory 
# render_template, session
import jinja2
import os
from werkzeug.utils import secure_filename
from convert import *

UPLOAD_FOLDER = 'uploads/csvs' #define a directory to upload files
DOWNLOAD_FOLDER = 'downloads/json'
ALLOWED_EXTENSIONS = {'csv'} #define which files are allowed to be uploaded

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    """Return homepage."""

    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['filename']
        upload = secure_filename(file.filename)
        file.save(os.path.join(app.config[UPLOAD_FOLDER], upload))
        writeDICTtoJSON(convertCSVtoDict(os.path.join(app.config[UPLOAD_FOLDER], upload), 'birddex_json'), 'BIRDDEX')
        flash('File uploaded.')
        return redirect('/')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


# @app.route('/csv-to-json', methods=['GET', 'POST'])
# def convert_csv_to_json():
#     """Convert the uploaded CSV file into a JSON file."""

#     data = request.form.get('body')
#     print(f"This is what's inside data (request.post):\n {data}")

    # return redirect('/')

    raise NotImplementedError("Functionality incomplete.")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4000)