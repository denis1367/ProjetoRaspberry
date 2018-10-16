#!/sbin/python
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
x=1
data=2

gpio.setmode(gpio.BCM)
gpio.setup(26,gpio.OUT)

#cont=0
#while cont < 1:
#for y in range(8):

gpio.output(26,1)
#time.sleep(0.1)
#gpio.output(5,1)
#time.sleep(0.1)
#gpio.output(5,0)
      # gpio.output(4,0)
       # gpio.output(6,1)
       # time.sleep(0.1)
       # gpio.output(6,0)
#print "acendendo"    
#        cont = cont+1
#for y in range(8):
#gpio.output(4,0)
#time.sleep(0.1)
#gpio.output(5,1)
#time.sleep(0.1)
#gpio.output(5,0)
#        gpio.output(4,0)
#        gpio.output(6,1)
#       time.sleep(0.1)
#        gpio.output(6,0)
#print "apagando"
