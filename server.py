from flask import Flask, render_template, request, redirect, url_for
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = set()  # Allow all file extensions
MAX_CONTENT_LENGTH = 10 * 1024 * 1024 * 1024  # 10GB limit

app.config['UPLOAD_FOLDER'] = 'files'
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return True  # Allow all file extensions

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/files', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Ensure a secure filename
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Check if the file size is within the limit
        if os.path.getsize(file_path) < app.config['MAX_CONTENT_LENGTH']:
            file.save(file_path)
            return redirect(url_for('index'))
        else:
            return "File size exceeds the limit (10GB)."

    return redirect(request.url)

@app.route('/download/<filename>')
def download_file(filename):
    return redirect(url_for('static', filename='files/' + filename, _external=True))

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))