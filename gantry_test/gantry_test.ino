#include <uStepperS.h>

uStepperS stepper;
float angle = 360.0;
uint8_t current_position = 1;

void setup() {
  // put your setup code here, to run once:
  stepper.setup();
  stepper.setMaxAcceleration(2000);
  stepper.setMaxVelocity(500);
  Serial.begin(9600);
  Serial.println(current_position);
}

void loop() {
  char cmd;
  // put your main code here, to run repeatedly:
  while(!Serial.available());
  cmd = Serial.read();
  if(cmd == '1')
  {
    move_up_position();
    Serial.println(current_position);
  }
  
  else if(cmd == '2')
  {
    move_down_position();
    Serial.println(current_position);
  }
  
  else if(cmd == '3')
  {
    move_home();
    Serial.println(current_position);
  }

  else if(cmd == '4')
  {
    stepper.moveAngle(-angle);
  }

  else if(cmd == '5')
  {
    stepper.moveAngle(angle);
  }
}

void move_home(){
  if (current_position == 1){
    Serial.println("Already at Home");
  }
  else{
    stepper.moveAngle(angle*4*(current_position-1));
    current_position = 1;
  }
}

void move_up_position(){
  if (current_position == 4){
    Serial.println("End of the line");
  }
  else{
    stepper.moveAngle(-angle*4);
    current_position = current_position + 1;
  } 
}

void move_down_position(){
  if (current_position == 1){
    Serial.println("Already at Home");
  }
  else{
    stepper.moveAngle(angle*4);
    current_position = current_position - 1;
  } 
}

