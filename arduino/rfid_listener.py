# save as rfid_listener.py
import serial
import time

PORT = "COM3"        # <-- change this to your Arduino port
BAUD = 9600
TIMEOUT = 1

def main():
    try:
        ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)
        print(f"Listening on {PORT} @ {BAUD}...")
        last_msg = None
        while True:
            line = ser.readline().decode(errors='ignore').strip()
            if not line:
                continue
            # Basic parsing: "scanned,AF E1 98 1F" or "null"ṇṇ
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

            # print only on change (avoid duplicate prints)
            if msg != last_msg:
                if msg[0] == "scanned":
                    print(f"[{time.strftime('%H:%M:%S')}] SCANNED -> UID: {msg[1]}")
                    # TODO: handle scanned event (log, call API, DB etc.)
                elif msg[0] == "null":
                    print(f"[{time.strftime('%H:%M:%S')}] NULL (card removed)")
                    # TODO: handle removal event
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] {msg[1]}")
                last_msg = msg
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
