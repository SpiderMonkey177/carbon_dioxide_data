# carbon_dioxide_data

This is the software to run the NDIR Carbon Dioxide Data with the Raspberry Pi. Please follow instructions below. 

1. Run the below code on your Raspberry Pi to install the respective packages. 

$` sudo pip3 install adafruit-circuitpython-mcp3xxx

2. Connect the Pi-Hat and Raspberry Pi with the CO2 Sensor as displayed in the image below. 

<img src='https://i.ibb.co/rQmbpD3/IMG-3261.jpg' title='Connection' width='' alt='Walkthrough' />

3. Run "git clone" with it to retrieve this folder on your Raspberry pi. 

4. Run the following code on your terminal (in the folder carbon_dioxide_data). 

$` python3 code.py

5. Either enter if you have a "Pi-0" or "Full-sizedPi". This is **case-sensitive**. 

6. You should retrieve a JSON Dictionary with the milli-voltage count and the CO2 Concentration.

