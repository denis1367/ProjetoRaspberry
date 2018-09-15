from threading import 
import RPi.GPIO as gpio
import time
from datetime import datetime
import time
gpio.setmode(gpio.BCM)
gpio.setup(26,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(19,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(13,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(6,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(21,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(20,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(16,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(12,gpio.IN, pull_up_down = gpio.PUD_DOWN)

p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0
#1
def registrando(porta )
	now = datetime.now()
	porta = data_e_hora_em_texto = data_e_hora_atuais.strftime(‘%d/%m/%Y %H:%M:%S’)

def inputPorta(portaGpio):
	while true:

		inicio=tempo.time()
		while(gpio.input(portaGpio) == 1)
		fim = time.time()	
		print("fim - inicio")



# aqui salvar o arquivo

			# if(gpio.input(portaGpio) == 1):
			# 	print ("Luz acesssa")
	 	#     else:
	  #   		print("Luz apagada")

