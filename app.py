from flask import Flask, render_template
from dataAnalysis import makeData

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/data")
def data():
    dataTable = makeData()
    return render_template("data.html", dataTable=dataTable)
    
#@app.route("/Analysis")
#def analysis

if __name__ == "__main__":
    app.run(debug=True)
