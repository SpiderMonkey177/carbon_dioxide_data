import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

# create the spi bus

CLK = board.D21

MISO = board.D19

MOSI = board.D20

CS = board.D26

spi = busio.SPI(clock=CLK, MISO=MISO, MOSI=MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(CS)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

print('Raw ADC Value: ', chan.value)
print('ADC Voltage: ' + str(chan.voltage) + 'V')

#We need to receive the output from the raspberry pi. analogRead value. chan.value



#Convert the analog signal to a voltage. 


voltage = chan.value
print(voltage)

#Convert the voltage to a PPM read. 

#only if the voltage is larger than 400. 

data_set = {"CO2concentration": [], "VoltageDifference": []}

for i in range(10):
    if voltage < 400:
        array.append("preheating")
    else:
        voltageDifference = voltage - 400
        concentration = (voltageDifference*50)/16
        data_set["CO2concentration"].append(concentration)
    time.sleep(1)

print(data_set)


# int voltage_diference=voltage-400;
# float concentration=voltage_diference*50.0/16.0;

#create a pandas dataframe and append it on the dataframe. 

#delay it 1000. 


