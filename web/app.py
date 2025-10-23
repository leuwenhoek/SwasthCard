import os
import json
from flask import Flask, render_template, request, redirect, jsonify
from os.path import dirname, join, abspath
from datetime import date,datetime

# Mymodules
import sys
sys.path.append(abspath(join(dirname(__file__), '..')))
from modules import myjson
from modules import rfid_listener

app = Flask(__name__)
app.secret_key = "mysec"

# Global locations
PATIENT_JSON = os.path.join("database", "patient_profile.json")
DOCTOR_JSON = os.path.join("database", "doctor_profile.json")
RFID_JSON = os.path.join("database", "RFID_status.json")

# Initialize JSON files
def init_JSON():
    jn = myjson.JSON()
    if not os.path.exists('database'):
        os.mkdir("database")
    JSON_FOLDER = os.path.join("database")
    
    if not os.path.exists(os.path.join(JSON_FOLDER,"patient_profile.json")):
        jn.create_JSON(JSON_FOLDER, "patient_profile.json","paitent profile")
        
    if not os.path.exists(os.path.join(JSON_FOLDER,"doctor_profile.json")):
        jn.create_JSON(JSON_FOLDER, "doctor_profile.json","doctor profile")

    jn.create_JSON(JSON_FOLDER, "RFID_status.json","RFID status")
    jn.create_JSON(JSON_FOLDER, "Symptoms.json","console")

# Login credentials (TODO: Move to secure storage)
doc_id = "1234"
doc_pass = "1234"
patient_id = "2025"
patient_pass = "Ayush"
patient_name = "Ayush"

# Send user to home page
@app.route("/", methods=["GET", "POST"])
def home():
    role = request.form.get('role')
    if role == "doctor":
        return redirect("/doctor_login")
    elif role == "patient":
        return redirect("/patient_login")
    return render_template("Home.html")

# Doctor login
@app.route("/doctor_login", methods=["GET", "POST"])
def doctor():
    if request.method == "POST":
        doctor_code = request.form.get('code')
        password = request.form.get('pass')
        if doctor_code == doc_id and password == doc_pass:
            return redirect("/doctor_profile")
    return render_template("Doctor_login.html")

# Patient login
@app.route("/patient_login", methods=["GET", "POST"])
def patient():
    if request.method == "POST":
        RFID_num = request.form.get('num')
        password = request.form.get('pass')
        if RFID_num == patient_id and password == patient_pass:
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

# Doctor profile
@app.route("/doctor_profile", methods=["GET", "POST"])
def doctor_profile():
    try:
        with open(DOCTOR_JSON, 'r') as file:
            doctor_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading doctor profile: {e}")
        doctor_data = {
            "doctor_name": "Data Not Found",
            "specialization": "N/A",
            "total_patients_treated": 0,
            "patients_treated": []
        }

    if request.method == "POST" and request.form.get('action') == "add_patient_request":
        return redirect('/patient_registration')
    
    return render_template("Doctor_profile.html", doctor=doctor_data)

# AI suggestion page
@app.route("/AI_suggestion")
def AI():
    return render_template("AI_page.html")

# Patient registration
@app.route("/patient_registration", methods=["GET", "POST"])
def registration():
    message = ""
    if request.method == "POST":
        RFID_num = request.form.get('rfidNumber')
        name = request.form.get('patientName')
        if RFID_num == patient_id and name == patient_name:
            return redirect("/doc_console")
        else:
            message = "Incorrect Credentials"
    return render_template("Patient_registration.html", message=message)

@app.route("/rfid_status")
def get_rfid_status():
    try:
        with open(RFID_JSON, "r") as f:
            rf = json.load(f)
            status = rf.get("Status", "offline")
    except Exception:
        status = "offline"
    return jsonify({"status": status})


# Modified doctor console route:
@app.route("/doc_console", methods=["GET", "POST"])
def console():
    # If GET: check RFID status first. If not online -> show blocker waiting page
    if request.method == "GET":
        try:
            with open(RFID_JSON, "r") as f:
                rf = json.load(f)
                status = rf.get("Status", "offline")
        except Exception:
            status = "offline"

        if status != "online":
            # Show waiting page until card goes online.
            # Pass the expected patient_id (here global) so template shows "Waiting for card '2025'"
            return render_template("waiting_for_card.html", waiting_id=patient_id)

        # else fallthrough to render the console page (GET + status online)
        return render_template("console.html")

    # If POST: keep your original POST handling for console
    if request.method == "POST":
        try:
            data = request.get_json(force=True)
            patient_id_req = data.get("patient_id", "")
            symptoms_string = data.get("symptoms", "")
            # Split the comma-separated string into a list for processing
            symptoms_list = [s.strip() for s in symptoms_string.split(",") if s.strip()]
            print(f"Received data: patient_id={patient_id_req}, symptoms={symptoms_list}")

            location = os.path.join("database", "Symptoms.json")
            symptoms_str = ",".join(symptoms_list)
            symptom_data = {
                "symptoms": symptoms_str,
                "date_time": f"{date.today()} {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                "conclusion": "N/A",
                "location": "MAX delhi"
            }
            with open(location, "w") as f:
                json.dump(symptom_data, f, indent=4)
            return jsonify({"status": "ok", "patient_id": patient_id_req, "symptoms": symptoms_list})

        except Exception as e:
            print(f"Error processing request: {e}")
            return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    init_JSON()
    app.run(debug=True)