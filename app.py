from flask import Flask, render_template, flash, request, redirect, url_for
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route('/sort/selection', methods=['GET', 'POST'])
def upload_file():
    return "HALO"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_route_summary():
    if request.method == 'POST':
        csv_dicts = "Apa kabar"
    return redirect('/', csv_dicts = csv_dicts)



if __name__ == "__main__":
    app.run(debug=True)