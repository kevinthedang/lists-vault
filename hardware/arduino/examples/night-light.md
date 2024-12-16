<div align="center">
  <p><a href="https://www.arduino.cc/"><img alt="arduino-icon" src="../../../media/hardware/arduino/arduino.svg" width="150px"/></a></p>
  <h1>Night Light Example</h1>
  <h4>Toggling an LED with an LDR</h4>
</div>

### Overview
The Arduino Night Light project is a great example that demonstrates how to build an automated light that turns on in the dark and off in bright environments.

### Materials
* An Arduino Uno
* Any 2-pin LED.
* A 220 ohm resistor and a 10k ohm resistor.
* A 2-pin photoresistor.
* A USB 2.0 Cable Type A/B
* Some wires! You should have Red and Black as a must to differentiate live and ground wires.

### Wiring Diagram
<div align="center">
    <img alt="night-light-circuit" src="../../../media/hardware/arduino/examples/night-light-circuit.svg"/>
</div>

### Code to Run
The following is the code used to work with the project. Variations can be made to this. Instead of immediately turning off you can have it slowly dim. Remove `Serial.println(lightLevel)` to do this.

```cpp
// Define pins
const int LDR_PIN = A0; // Photoresistor connected to analog pin A0
const int LED_PIN = 9;  // LED connected to digital pin 9

// Threshold value for sensor
const int LIGHT_THRESHOLD = 500;

void setup() {
  pinMode(LED_PIN, OUTPUT);   // Configure digital pin 9 as an output to control an LED or other device
  Serial.begin(9600);         // Start serial communication at 9600 bits per second for debugging or data monitoring
}

void loop() {
  int lightLevel = analogRead(LDR_PIN); // Read the value from the sensor connected to A0 (ranges from 0 to 1023)

  Serial.println(lightLevel);
  
  // Check if the sensor value exceeds the threshold
  if (lightLevel < LIGHT_THRESHOLD) {
    digitalWrite(9, HIGH); // Turn on the LED
  } else {
    digitalWrite(9, LOW); // Turn off the LED
  }

  // Stability in case of rapid flickering
  delay(100);
}
```