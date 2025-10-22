#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 rfid(SS_PIN, RST_PIN);

bool cardPresent = false;
String lastUID = "";

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  delay(50);
  Serial.println("Ready");
}

String uidToString(MFRC522::Uid uid) {
  String s = "";
  for (byte i = 0; i < uid.size; i++) {
    if (uid.uidByte[i] < 0x10) s += "0";
    s += String(uid.uidByte[i], HEX);
    if (i < uid.size - 1) s += " ";
  }
  s.toUpperCase();
  return s;
}

void loop() {
  bool detected = false;
  String currentUID = "";

  // check for card
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    currentUID = uidToString(rfid.uid);
    detected = true;
    rfid.PICC_HaltA(); // stop current card
  }

  if (detected) {
    // if previously no card or different UID -> new scan event
    if (!cardPresent || currentUID != lastUID) {
      lastUID = currentUID;
      cardPresent = true;
      // Send scanned and UID in one line, comma separated
      Serial.print("scanned,");
      Serial.println(lastUID);
    }
  } else {
    // no card detected now
    if (cardPresent) {
      // card was present earlier, now removed -> send null once
      Serial.println("null");
      cardPresent = false;
      lastUID = "";
    }
  }

  delay(200); // small debounce / reduce serial spam
}
