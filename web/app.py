from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    role = request.form.get('role')
    print(role)
    if role == "doctor":
        return redirect("/doctor_login")
    elif role == "patient":
        return redirect("/patient_login")
    return render_template("Home.html")

@app.route("/doctor_login",methods=["GET","POST"])
def doctor():
    return render_template("Doctor_login.html")

@app.route("/patient_login",methods=["GET","POST"])
def patient():
    return render_template("Patient_login.html")

@app.route("/profile")
def profile():
    return "0"

if __name__ == "__main__":
    app.run(debug=True)