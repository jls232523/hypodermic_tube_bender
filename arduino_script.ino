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
  // Homing
  //while (digitalRead(limitSwitch) != 0) {
      //Serial.print("yo");

    //benderStepper.setSpeed(1200);
    //benderStepper.runSpeed();
    //benderStepper.setCurrentPosition(0); // When limit switch pressed set position to 0 steps
 // }
  delay(1000);
  // Move 1400 steps from the limit switch to starting position
 // while (benderStepper.currentPosition() != -1400) {
   // benderStepper.setSpeed(-1200); // if negative rotates anti-clockwise
    //benderStepper.run();
 // }
  //benderStepper.setCurrentPosition(0);
}

void loop() {
  String mode = "tube";
  if (mode.startsWith("tube")) {
 
    tube();
  }
 
}
void tube(){
 int feed = 7.718; //mm
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
    while (benderStepper.currentPosition() !=75* angleConst) {// 1st bend left
      benderStepper.setSpeed(1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);
    
// Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=-5* angleConst) {// 1st bend left
      benderStepper.setSpeed(-1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);


    
    servo01.write(130);                                       // down
        delay(500);




    feed = 21.8186;
    Serial.println("Feed side1");
    feedDistance =  feed *48;
    while (feederStepper.currentPosition() != feedDistance) { //feed
      feederStepper.setSpeed(1000);
      feederStepper.run();
    }
 
 
        
// Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=10* angleConst) {// move to the other side of tube
      benderStepper.setSpeed(1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);

        
     

  
 servo01.write(5);                                           // Up
  delay(500);



                                                                                                    // second bend
    // Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=-135* angleConst) {// 2nd bend 
      benderStepper.setSpeed(-1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);




 
    servo01.write(130);                                         // down
        delay(500);



feed = 29.8704;
    Serial.println("Feed topside");
    feedDistance =  feed *48;
    while (feederStepper.currentPosition() != feedDistance) {   // Feed
      feederStepper.setSpeed(1000);
      feederStepper.run();
    }





 









                                                                                                   // reset
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
    while (benderStepper.currentPosition() !=-50* angleConst) {// 3rd bend left
      benderStepper.setSpeed(-1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);




 // down
    servo01.write(130);
        delay(500);

feedStepper.setCurrentPosition(0);
//feed = 7.1882; //mm
//    feedDistance = feed * 48;
// while (feederStepper.currentPosition() != feedDistance) { // run until it reaches the distance value
//      feederStepper.setSpeed(1200);
//      feederStepper.run();
//    }
feedStepper.setCurrentPosition(0);


servo01.write(5); // Set the bender pin up
  delay(500);

    // Bend the wire 45 degrees
    benderStepper.setCurrentPosition(0);
    while (benderStepper.currentPosition() !=95* angleConst) {// 4th bend left
      benderStepper.setSpeed(1200);
      Serial.println("65\n");
      benderStepper.run();
    }
    benderStepper.setCurrentPosition(0);
    delay(100);

    
    while(1){
      Serial.println("done");
    }
 
}
python-build-end
