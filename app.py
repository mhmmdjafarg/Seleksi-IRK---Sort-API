from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import json
from ast import literal_eval

# import created function
from IOprocess import *
from algorithm import *
from database import *

app = Flask(__name__)
app.secret_key = "IRK" #random secret key, can be anything
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #Max content length = 16 mb
# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads') #the directory name will be 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create connection
conn = create_db_connection()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sort/<method>', methods=['POST'])
def upload_file(method):
    uploadedfile = request.files['file']
    kolomacuan = int(request.form['kolomacuan'])-1
    orientasi = request.form['orientasi']
    algoritma = method
    if uploadedfile.filename != '':
        filename = secure_filename(uploadedfile.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        jsonarray = convertCSV(file_path)
    
    # Validasi kolom acuan
    column = len(list(jsonarray[0].keys()))
    if (kolomacuan >= column):
        return redirect('/')

    # SORT
    if (method == 'selection'):
        data, exectime = selectionsort(jsonarray, kolomacuan, orientasi)
    elif (method == 'bubble'):
        data,exectime = bubbleSort(jsonarray, kolomacuan, orientasi)
    else:
        return "<h1>Method %s not recognized </h1>" %method

    insertData(conn, jsonarray, method, exectime)
    keys = list(data[0].keys())
    return render_template('result.html',data = data, keys = keys)

@app.route('/sort/result', methods=['GET'])
def showresult():
    # if key doesn't exist, returns None
    id = request.args.get('id')
    if(id == None):
        id = getLastId(conn)
    databyte = getdata(conn,int(id))
    if(databyte == 'No data'):
        return "<h1>Id %s not found  </h1>" %id
    jsonData = databyte.decode('utf8').replace("'", '"')
    data = json.loads(jsonData)
    data = json.dumps(data)
    finaldata = literal_eval(data)
    keys = list(finaldata[0].keys())
    return render_template('result.html', data= finaldata, keys=keys)

if __name__ == "__main__":
    app.run(debug=True)