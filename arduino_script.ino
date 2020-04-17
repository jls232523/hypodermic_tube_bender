// python-build-start
// upload
// arduino:avr:uno
// /dev/cu.usbmodem1411
// python-build-end
#include <AccelStepper.h>
#include <Servo.h>

#define limitSwitch 11

// Define the stepper motors and the pins the will use
AccelStepper feederStepper(1, 5, 6); // (Type:driver, STEP, DIR)
AccelStepper zAxisStepper(1, 7, 8);
AccelStepper benderStepper(1, 9, 10);

Servo servo01;
String dataIn = "";
String manualStatus = "";
int count = 0;
int dist;

void setup() {
  Serial.begin(9600);
  //pinMode(limitSwitch, INPUT_PULLUP);
  servo01.attach(3);
  //servo01.write(0); // Initial position, bending pin up
  
  // Stepper motors max speed
  feederStepper.setMaxSpeed(1000);
  zAxisStepper.setMaxSpeed(1000);
  benderStepper.setMaxSpeed(1000);
  delay(1000);
}

void loop() {
  String mode = "tube";
  if (mode.startsWith("tube")) { 
    tube();
  }
}
void tube(){
 int feed = ~ ; //mm
 int feedDistance = feed * 48;

  feederStepper.setCurrentPosition(0); //reset
 while (feederStepper.currentPosition() != feedDistance) { // run until it reaches the distance value
      feederStepper.setSpeed(1000);
      feederStepper.run();
    }
 feederStepper.setCurrentPosition(0); //reset

   servo01.write(0); // Set the bender pin up
    delay(500);

    int angleConst = 18; // angle constant

   servo01.write(5); // Set the bender pin up
    delay(500); 
    // Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() != ~ * angleConst) {// 1st bend left positive
      benderStepper.setSpeed(1200);
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);

    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=-5* angleConst) {// Move away from tube
      benderStepper.setSpeed(-1200);
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);
    servo01.write(130);                                       // down
        delay(500);
    feed = ~ ; // feed side 1
    Serial.println("Feed side1");
    feedDistance =  feed *48;
    while (feederStepper.currentPosition() != feedDistance) { //feed
      feederStepper.setSpeed(1000);
      feederStepper.run();
    }   
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=10* angleConst) {// move to the other side of tube
      benderStepper.setSpeed(1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);
 servo01.write(5);                                           // Up
  delay(500);                                                                                              // second bend
    // Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() != ~ * angleConst) {// 2nd bend negative
      benderStepper.setSpeed(-1200);
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);
    servo01.write(130);                                         // down
        delay(500);
feed = ~ ; //feed top length
    feedDistance =  feed *48;
    while (feederStepper.currentPosition() != feedDistance) {   // Feed
      feederStepper.setSpeed(1000);
      feederStepper.run();
    }                                                                                      // reset
 // Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=85* angleConst) {// reset bender
      benderStepper.setSpeed(1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(1000);////////////////////////////////////////////////////////////////////////////////////
servo01.write(5);                                             // Set the bender pin up
  delay(500);

// Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() != ~ * angleConst) {// 3rd bend left negative
      benderStepper.setSpeed(-1200);
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);
 // down
    servo01.write(130);
        delay(500);

feedStepper.setCurrentPosition(0);

servo01.write(5); // Set the bender pin up
  delay(500);

    // Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() != ~ * angleConst) {// 4th bend left positive
      benderStepper.setSpeed(1200);
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);
    while(1){
      Serial.println("done");
    }
 
}
