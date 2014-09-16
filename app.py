from flask import Flask, render_template

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/data")
def data():
    dataTable = ""
    f = open('data/data.csv', 'r')
    line = f.readline()
    while line:
        dataTable += '<tr>'
        for i in line.split(',')[:-1]:
            dataTable += ('<td>' + str(i) + '</td>')
            dataTable += '</tr>'
            line = f.readline()
    return render_template("data.html", dataTable=dataTable)
    
#@app.route("/Analysis")
#def analysis

if __name__ == "__main__":
    app.run(debug=True)
