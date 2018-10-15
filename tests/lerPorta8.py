import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(SPI_PORT. SPI_DEVICE))
#INICIANDO VARIAVEIS
sensibilidade = 0.66
voltagePunidade = 5/1023
vcc = 1024/2

while True:
	data = mcp.read_adc(8)
	print("VALOR DO CANAL 8 :", DATA)
	conversao = ((mcp.read_adc(8))*(voltagePunidade/sensivilidade))
	print("DADOS DEPOIS DA CONVERSAO: " .conversao)
