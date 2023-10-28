import os, getlinks
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', links = getlinks.getlinks())


@app.route('/download/<path:filename>')
def download(filename):
    return send_file("ftp/" + filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port='5000')

