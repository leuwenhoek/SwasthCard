import serial
import time
import json
import os

PORT = "COM3"        # <-- change this to your Arduino port
BAUD = 9600
TIMEOUT = 1
JSON_FILE = "path/to/status.json"  # <-- replace with your JSON file path
DEBOUNCE_SECONDS = 2  # Time to wait before confirming card removal

def update_json_status(status):
    """Update the JSON file with the given status."""
    status_data = {"status": status}
    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(status_data, f)
    except Exception as e:
        print(f"Error updating JSON file: {e}")

def main():
    try:
        ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)
        print(f"Listening on {PORT} @ {BAUD}...")
        last_msg = None
        null_start_time = None  # Track when null state starts
        is_offline = False     # Track current JSON status

        while True:
            line = ser.readline().decode(errors='ignore').strip()
            if not line:
                continue
            # Basic parsing: "scanned,AF E1 98 1F" or "null"
            if line.startswith("scanned"):
                # split and get UID part
                parts = line.split(",", 1)
                uid = parts[1].strip() if len(parts) > 1 else ""
                msg = ("scanned", uid)
            elif line == "null":
                msg = ("null", "")
            else:
                # ignore or print unknown lines
                msg = ("other", line)

            # Handle state changes with debounce for null
            current_time = time.time()
            if msg != last_msg:
                if msg[0] == "scanned":
                    null_start_time = None  # Reset null timer
                    if last_msg != msg:  # Only print/update if state changed
                        print(f"[{time.strftime('%H:%M:%S')}] SCANNED -> UID: {msg[1]}")
                        if is_offline:
                            update_json_status("online")
                            is_offline = False
                        print("s")  # Card is being scanned
                elif msg[0] == "null":
                    if null_start_time is None:
                        null_start_time = current_time  # Start null timer
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] {msg[1]}")
                last_msg = msg

            # Check if null state has persisted long enough
            if msg[0] == "null" and null_start_time is not None:
                if current_time - null_start_time >= DEBOUNCE_SECONDS:
                    if not is_offline:  # Only print/update if not already offline
                        print(f"[{time.strftime('%H:%M:%S')}] NULL (card removed)")
                        update_json_status("offline")
                        print("n")  # Card is confirmed removed
                        is_offline = True

    except serial.SerialException as e:
        print("Serial error:", e)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        try:
            ser.close()
        except:
            pass

if __name__ == "__main__":
    main()