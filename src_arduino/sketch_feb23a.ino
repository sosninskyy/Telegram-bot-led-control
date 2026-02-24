const byte red[] = {8,9,10};
const byte green[] = {2,3,4};

void setup() {

  Serial.begin(9600);
  for (int i = 0; i < 3; i++) {
    pinMode(red[i], OUTPUT);
    pinMode(green[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    if (data == '1') red_part();
    else if (data == '2') green_part();
    else if (data == '3') both_part();
  }
}

void setLightState(const byte array[], bool state) {
  for (int i = 0; i < 3; i++) {
    digitalWrite(array[i], state ? HIGH : LOW);
  }
}

void red_part() {
  setLightState(red, true);
  delay(500);
  setLightState(red, false);
}


void green_part() {
  setLightState(green, true);
  delay(500);
  setLightState(green, false);
}


void both_part() {
  setLightState(green, true);
  setLightState(red, true);
  delay(500);
  setLightState(green, false);
  setLightState(red, false);
}
