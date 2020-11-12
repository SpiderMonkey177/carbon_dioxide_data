import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

print('Raw ADC Value: ', chan.value)
print('ADC Voltage: ' + str(chan.voltage) + 'V')

#We need to receive the output from the raspberry pi. analogRead value. chan.value



#Convert the analog signal to a voltage. 


voltage = chan.value*(5000/1024)

#Convert the voltage to a PPM read. 

#only if the voltage is larger than 400. 

array = []

for i in range(200)
    if voltage < 400:
        array.append("preheating")
    else:
        voltageDifference = voltage - 400
        concentration = voltageDifference*50/16





# int voltage_diference=voltage-400;
# float concentration=voltage_diference*50.0/16.0;

#create a pandas dataframe and append it on the dataframe. 

#delay it 1000. 


