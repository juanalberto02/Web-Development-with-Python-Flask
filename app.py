from flask import Flask, redirect, url_for, request, render_template ,send_file, flash, jsonify, send_from_directory
import math
import csv  

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


@app.route("/")
def halaman1():
    return render_template("index.html")
    
@app.route("/index.html")
def halaman_1():
    return render_template("index.html")

@app.route("/calculator.html")
def halaman2():
    flash(" ")
    return render_template("calculator.html")

@app.route("/akar", methods=['POST', 'GET'])
def akar():
    number1 = str(request.form['angka'])
    number = int(request.form['angka'])
    number = math.sqrt(number)
    number = str(number)
    flash("Akar dari " + number1 + " adalah "+ number)
    return render_template("calculator.html")

@app.route("/data.html")
def halaman_3():
    return render_template("data.html")

@app.route('/convert', methods = ['GET', 'POST'])
def convert():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

    data = {}
    data1 = str(data)
    with open(f.filename) as csvFile:                     
        csvReader = csv.DictReader(csvFile)
        for i, rows in enumerate(csvReader):
            id = i
            data[id] = rows

    return jsonify(data)

@app.route("/form.html")
def halaman4():
    return render_template("form.html")


@app.route("/feedback", methods=['POST', 'GET'])
def feedback():
    nama = request.form['nama']
    komen = request.form['komen']
    flash("")
    flash(nama + "  berkomentar bahwa :  ")
    flash(komen)
    return render_template("form.html")       



if __name__ == "__main__":
    app.run(debug=True)
