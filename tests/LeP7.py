import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 0
SPI_DEVICE = 0

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


sensibilidade = 0.066
voltagePunit = 5/1023
vcc = 1024/2
while True:
        data = mcp.read_adc(6)
        print(" PORTA 6:", data)
        conversao = ((mcp.read_adc(6) - vcc)*(voltagePunit/sensibilidade))
#        print("data convetido: " ,conversao)
        time.sleep(0.8)
