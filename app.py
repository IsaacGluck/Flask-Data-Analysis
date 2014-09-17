from flask import Flask, render_template, request

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['b']
        name = request.form['name']
        if button=="cancel":
            return render_template("login.html")
        else:
            return render_template("data.html", name = name)

@app.route("/data")
def data():
    return render_template("data.html", name = "Z")
    
@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

if __name__ == "__main__":
    app.run(debug=True)
