import os
from flask import Flask,render_template,request,redirect,url_for
import sys
from os.path import dirname, join, abspath

# Mymodules
sys.path.append(abspath(join(dirname(__file__), '..')))
from modules import myjson

app = Flask(__name__)

# Initializing JSON
def init_JSON():
    jn = myjson.JSON()
    if not os.path.exists('database'):
        os.mkdir("database")
    JSON_FOLDER = os.path.join("database")
    jn.create_JSON(JSON_FOLDER,"patient_profile.json")
    jn.create_JSON(JSON_FOLDER,"doctor_profile.json")

# Global locations
PATIENT_JSON = os.path.join("database","patient_profile.json")
DOCTOR_JSON = os.path.join("database","doctor_profile.json")

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
    init_JSON()
    app.run(debug=True)