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
            authenticate.register(name, password)
            if authenticate.authentic(name, password) == "NP":
                print "NP"
                return render_template("login.html")
            if authenticate.authentic(name, password) == "NR":
                print "NR"
                return render_template("login.html")
            return render_template("data.html", name = name)

@app.route("/data")
def data():
    return render_template("data.html", name = name)
    
@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

if __name__ == "__main__":
    app.run(debug=True)
