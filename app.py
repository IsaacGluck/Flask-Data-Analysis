from flask import Flask, render_template, request
import authenticate

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['b']
        global name
        name = request.form['name']
        password = request.form['password']
        if button=="cancel":
            return render_template("login.html")
        else:
            if authenticate.authentic(name):
                return render_template("data.html", name = name)
            return render_template("login.html")


f = open('data/data.csv', 'r')

@app.route("/data")
def data():
    dataList = [];
    line = f.readline()
    while line:
        tmpList = []

        for i in line.split(','):
            tmpList.append(str(i))

        dataList.append(tmpList)
        line = f.readline()
    return render_template("data.html", dataList = dataList, name = name)
f.close()

t = open('data/data2.csv', 'r')

@app.route("/analysis")
def analysis():
    dataList = [];
    line = t.readline()
    while line:
        tmpList = []

        for i in line.split(','):
            tmpList.append(str(i))

        dataList.append(tmpList)
        line = t.readline()
    return render_template("analysis.html", dataList = dataList)

if __name__ == "__main__":
    app.run(debug=True)
