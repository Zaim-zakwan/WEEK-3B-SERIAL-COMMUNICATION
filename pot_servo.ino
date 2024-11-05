const int potPin = A0;
#include <Servo.h>
Servo servo;
int value = 0;         
int angle = 0;

void setup() {
  // put your setup code here, to run once:
  servo.attach(9);
  pinMode(9, OUTPUT);
  pinMode(potPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  value = analogRead(potPin);
  angle = map(value, 0, 1023, 0, 180);
  Serial.println(angle);
  servo.write(angle);
  delay(200) ;
}
