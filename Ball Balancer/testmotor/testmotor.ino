#include<Servo.h>
#include<PID_v1.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
String content = "110";
String content2 = "80";
byte flag = 0;
byte motorP1 = 4;
byte motorP2 = 5;
Servo m[2];

double angle[2]={80,110},input[2];
PID mPID1(&input[0],&angle[0],0,2,5,1,DIRECT);
PID mPID2(&input[1],&angle[1],0,2,5,1,DIRECT);

void setup() {
  m[0].attach(motorP1);
  m[1].attach(motorP2);
  Serial.begin(115200);
  mPID1.SetMode(AUTOMATIC);
  mPID2.SetMode(AUTOMATIC);
  lcd.init(); //initialize the lcd
  lcd.backlight(); //open the backlight
}

void loop() {
  //  while (Serial.available() > 0) {
  //    byte size = Serial.readBytes(input, 30);
  //    input[size] = 0;
  //    command = strtok(input, " ");
  //  }
  //  int i = 0;
  //  while (command != NULL) {
  //    angle[i] = atoi(command);
  //    Serial.println(angle[i]);
  //    m[i].write(angle[i]);
  //    i++;
  //    command = strtok(NULL, " ");
  //  }
  while (Serial.available()) {
    char ch = Serial.read();
    if (ch == 'i') {
      flag = 1;
      delay(1);
      ch = Serial.read();
    }
    if (ch == 'm') {
      flag = 2;
      delay(1);
      ch = Serial.read();
    }

    if (ch == 'e') flag = 3; 
    if (flag == 1) {
      content.concat(ch);
    }
    else if (flag == 2) {
      content2.concat(ch);
    }
    else if (flag == 3) {
      lcd.clear();
      angle[0]=content.toInt();
      //mPID1.Compute();
     
      lcd.setCursor(0, 0);
      lcd.print(angle[0]);
      content = "";
      angle[1]=content2.toInt();
      //mPID2.Compute();
      
      lcd.setCursor(0, 1);
      lcd.print(angle[1]);
      content2 = "";
    }
  }
   m[0].write(angle[0]);
   m[1].write(angle[1]);
  
}

