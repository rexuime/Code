import serial 
import time 


# change port to whatever COM arduino is on
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1) 

def write_read(x): 
	
    #arduino.write(b'Hello World')
	arduino.write(bytes(x, 'utf-8')) 
	time.sleep(0.05) 
	data = arduino.readline() 
	return data 

while True: 
	
	num = input("Enter a number: ") # Taking input from user 
	value = write_read(num) 
	print(value) # printing the value 


# Arduino Code
	
"""
int x; 

void setup() { 
	Serial.begin(115200); 
	Serial.setTimeout(1); 
} 

void loop() { 
	while (!Serial.available()); 
	x = Serial.readString().toInt(); 
	Serial.print(x + 1); 
} 
"""