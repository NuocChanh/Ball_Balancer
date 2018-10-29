#include <Servo.h>
Servo servoX;
Servo servoY;
int pos = 0;
int button = 3;
void setup() {
  servoX.attach(4);
  servoY.attach(5);
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) {
    servoX.write(pos);
    delay(15);
  }
  for (pos = 180; pos >= 0; pos -= 1) {
    servoY.write(pos);
    delay(15);
  }
}
/*
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
 */
