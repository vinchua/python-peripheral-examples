void setup() {
  Serial.begin(115200);
}

void loop() {
  if(Serial.available() > 0){
    String str = Serial.readString();
    if(str.equals("Hello from Atlas 200 DK\n")){
      Serial.println("Arduino: Hello from Arduino");
    }
  }
}
