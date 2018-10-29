void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(30,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    char data = Serial.read();
    if (data=='1') digitalWrite(30,false);
    else digitalWrite(30,true);
    char str[2];
    str[0] = data;
    str[1] = '\0';
    Serial.print(str);
  }
}
