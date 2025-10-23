import serial
import json
import time
import os
import threading

PORT = "COM3"
BAUD = 9600
TIMEOUT = 1
STATUS_PATH = os.path.join("database", "RFID_status.json")

tap_count = 0  # global tap counter

def update_status(state):
    data = {}
    if os.path.exists(STATUS_PATH):
        with open(STATUS_PATH, "r") as f:
            try:
                data = json.load(f)
            except:
                data = {}
    data["Status"] = state
    with open(STATUS_PATH, "w") as f:
        json.dump(data, f, indent=4)

def listen():
    global tap_count
    try:
        ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)
        print(f"[RFID] Listening on {PORT} @ {BAUD}...")

        while True:
            line = ser.readline().decode(errors="ignore").strip()
            
            # Ignore empty lines or Arduino init signals like "Ready"
            if line and line.lower() not in ["ready", "null"]:
                tap_count += 1

                if tap_count % 2 == 1:
                    update_status("online")
                    print(f"[RFID] Tap {tap_count}: {line} → Status: online")
                else:
                    update_status("offline")
                    print(f"[RFID] Tap {tap_count}: {line} → Status: offline")

            time.sleep(0.05)

    except Exception as e:
        print("[RFID] Serial error:", e)

def start_listener():
    """Start listener in background thread"""
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()
