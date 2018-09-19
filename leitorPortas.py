from threading import 
import RPi.GPIO as gpio
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

def inputPorta(portaGpio):
	while true:
		if(gpio.input(portaGpio) == 1)
		print ("Luz acesssa")
		teste
