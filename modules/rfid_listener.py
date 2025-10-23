import serial
import os
import json

PORT = "COM3"      # Change as per your setup
BAUD = 9600
TIMEOUT = 1

status_path = os.path.join('database', 'RFID_status.json')


def listen_for_card():
    """
    Listens to the serial port for RFID scan messages.
    Returns the scanned message when a card is detected.
    """
    try:
        ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)
        print(f"Listening on {PORT} @ {BAUD}...")

        while True:
            line = ser.readline().decode(errors='ignore').strip()
            if not line:
                continue

            if line.startswith("scanned"):
                parts = line.split(",", 1)
                uid = parts[1].strip() if len(parts) > 1 else ""
                message = f"Card scanned: {uid}"
                print(message)
                return message  # return when scanned

    except serial.SerialException as e:
        print("Serial error:", e)
        return None
    finally:
        try:
            ser.close()
        except:
            pass


def update_json(data):
    """Safely write to JSON file."""
    with open(status_path, 'w') as f:
        json.dump(data, f, indent=4)


def run_listener():
    """Main function to handle RFID status updates."""
    if not os.path.exists(status_path):
        print(f"File not found: {status_path}")
        return

    with open(status_path, 'r') as f:
        data = json.load(f)

    # Mark system as running
    data["Code"] = "Running"
    update_json(data)

    # Wait for card
    msg = listen_for_card()

    if msg and msg.startswith("Card scanned:"):
        uid = msg.split(":", 1)[1].strip()

        if uid == "AF E1 98 1F":
            data["Status"] = "online" if data.get("Status") == "offline" else "offline"
            update_json(data)
            print(f"Status updated to: {data['Status']}")
        else:
            print(f"Scanned different card: {uid}")
    else:
        print("No valid scan detected")

    # Mark system stopped
    data["Code"] = "Stopped"
    update_json(data)
    print("System stopped cleanly.")


# Run only if executed directly (not when imported)
if __name__ == "__main__":
    run_listener()
