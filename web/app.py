import os
import json
from flask import Flask, render_template, request, redirect, url_for
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
    
    if not os.path.exists(os.path.join(JSON_FOLDER,"patient_profile.json")):
        jn.create_JSON(JSON_FOLDER, "patient_profile.json")
        
    if not os.path.exists(os.path.join(JSON_FOLDER,"doctor_profile.json")):
        jn.create_JSON(JSON_FOLDER, "doctor_profile.json")

# Global locations
PATIENT_JSON = os.path.join("database", "patient_profile.json")
DOCTOR_JSON = os.path.join("database", "doctor_profile.json")

# Send user to home page that he/she is a doctor or patient
@app.route("/", methods=["GET", "POST"])
def home():
    role = request.form.get('role')
    if role == "doctor":
        return redirect("/doctor_login")
    elif role == "patient":
        return redirect("/patient_login")
    return render_template("Home.html")

# Login page for doctor and patient
@app.route("/doctor_login", methods=["GET", "POST"])
def doctor():
    doctor_code = request.form.get('code')
    password = request.form.get('pass')
    if doctor_code == "1234" and password == "1234":  # login pass is "doctor code : 1234" and "password : 1234"
        return redirect("/doctor_profile")
    return render_template("Doctor_login.html")

@app.route("/patient_login", methods=["GET", "POST"])
def patient():
    RFID_num = request.form.get('num')
    password = request.form.get('pass')
    if RFID_num == "2025" and password == "Ayush":  # login pass is "RFID Number : 2025" and "password : Ayush"
        return redirect("/patient_profile")
    return render_template("Patient_login.html")

# Profile of doctor and patient
@app.route("/patient_profile")
def patient_profile():
    try:
        with open(PATIENT_JSON, 'r') as file:
            patient_data = json.load(file)
        history = patient_data.get('history', [])
        generations = patient_data.get('generation_tree', {})  # Fixed: Use correct key with fallback to empty dict
    except FileNotFoundError:
        history = []
        generations = {}  # Fallback for missing file
    except json.JSONDecodeError:
        # Handle malformed JSON gracefully
        history = []
        generations = {}
    ai_suggestion_mode = request.args.get('AI') == 'true'
    if ai_suggestion_mode:
        return redirect("/AI_suggestion")
    return render_template("Patient_profile.html", history=history, generations=generations)

@app.route("/doctor_profile")
def doctor_profile():
    return "1"

@app.route("/AI_suggestion")
def AI():
    return render_template("Ai_page.html")

if __name__ == "__main__":
    init_JSON()
    app.run(debug=True)