 ARDUINO:

void setup(){
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}
void loop(){
  if(Serial.available()){
 
    switch(Serial.read()){
   
      case '0':digitalWrite(13,LOW);
              break;
      case '1':digitalWrite(13,HIGH);
              break;
      default: break;
    }
  }
}


PYTHON :

import serial
ser=serial.Serial('COM3', 9600)
while 1:
 val=raw_input("Introduzca 1 para encender y 0 para apagar LED: ")
 ser.write(val)