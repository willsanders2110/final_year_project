int sensorPin1 = A0;
int sensorPin2 = A1;
int sensorPin3 = A2;
int sensorPin4 = A3;
int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  char cmd;
  while(!Serial.available());
  cmd = Serial.read();

  if(cmd == '1')
  {
    sensorValue1 = analogRead(sensorPin1);
    Serial.println(sensorValue1);
  }

  else if(cmd == '2')
  {
    sensorValue2 = analogRead(sensorPin2);
    Serial.println(sensorValue2);
  }

  else if(cmd == '3')
  {
    sensorValue3 = analogRead(sensorPin3);
    Serial.println(sensorValue3);
  }

  else if(cmd == '4')
  {
    sensorValue4 = analogRead(sensorPin4);
    Serial.println(sensorValue4);
  }

  
}
