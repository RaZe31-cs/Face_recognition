void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
   if (Serial.read() == 1) {
    digitalWrite(13, HIGH);
    delay(1000);
   }
   if (Serial.read() == 0) {
    digitalWrite(13, LOW);
    delay(1000);
   }
   
}