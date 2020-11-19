import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

# create the spi bus

print("What device are you using - Pi-0 or Full-sizedPi")
print("Either enter Pi-0 or Full-sizedPi. Note that this is case-sensitive")

user_input = input()

if (user_input == "Pi-0"):
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

elif (user_input == "Full-sizedPi"):
    CLK = 18
    MISO = 23
    MOSI = 24
    CS = 25

    spi = busio.SPI(clock=CLK, MISO=MISO, MOSI=MOSI)

    cs = digitalio.DigitalInOut(CS)
    mcp = MCP.MCP3008(spi, cs)
    chan = AnalogIn(mcp, MCP.P0)




print('Raw ADC Value: ', chan.value)
print('ADC Voltage: ' + str(chan.voltage) + 'V')

#We need to receive the output from the raspberry pi. analogRead value. chan.value



#Convert the analog signal to a voltage. 


#Convert the voltage to a PPM read. 

#only if the voltage is larger than 400. 

data_set = {"CO2concentration": [], "VoltageDifference": [], "voltage": []}

for i in range(10):

    voltage = chan.voltage * 1000

    print(voltage)

    if voltage < 400:
        data_set["CO2concentration"].append("Preheating")
        data_set["VoltageDifference"].append("Preheating")
        data_set["voltage"].append("Preheating")

    else:
        voltageDifference = voltage - 400
        concentration = (voltageDifference*50)/16
        data_set["CO2concentration"].append(concentration)
        data_set["VoltageDifference"].append(voltageDifference)
        data_set["voltage"].append(voltage)
    time.sleep(1)

print(data_set)


# int voltage_diference=voltage-400;
# float concentration=voltage_diference*50.0/16.0;

#create a pandas dataframe and append it on the dataframe. 

#delay it 1000. 