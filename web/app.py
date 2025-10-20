import os
from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)

# send user to home page that he/she is a doctor or patient
@app.route("/",methods=["GET","POST"])
def home():
    role = request.form.get('role')
    if role == "doctor":
        return redirect("/doctor_login")
    elif role == "patient":
        return redirect("/patient_login")
    return render_template("Home.html")

#login page for doctor and patient 
@app.route("/doctor_login",methods=["GET","POST"])
def doctor():
    doctor_code = request.form.get('code')
    password = request.form.get('pass')
    if doctor_code == "1234" and password == "1234":  # login pass is "doctor code : 1234" and "password : 1234"
        return redirect("/doctor_profile")
    return render_template("Doctor_login.html")

@app.route("/patient_login",methods=["GET","POST"])
def patient():
    RFID_num = request.form.get('num')
    password = request.form.get('pass')
    print(RFID_num)
    print(password)
    if RFID_num == "2025" and password == "Ayush":  # login pass is "RFID Number : 2025" and "password : Ayush"
        return redirect("/paitent_profile")
    return render_template("Patient_login.html")

#profile of doctor and patient
@app.route("/paitent_profile")
def paitnet_profile():
    return "0"

@app.route("/doctor_profile")
def doctor_profile():
    return "1"

if __name__ == "__main__":
    app.run(debug=True)