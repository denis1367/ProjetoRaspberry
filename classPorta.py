#!/usr/bin
from threading import Thread
import RPi.GPIO as GPIO
import time
from Lampada import Lampada
from decimal import Decimal
lamp=Lampada(0,0,0,0,0)
pinzcr = 0
class classPorta(Thread):
    def __init__(self,lamp,numThread,pinzcr):
        self.lamp = Lampada(lamp.getNome(),lamp.getPgpio(),lamp.getStatus(),lamp.getNumRele(),lamp.getLumi())
        pinzcr = pinzcr
        Thread.__init__(self)
        GPIO.setup(lamp.getPgpio(),GPIO.OUT)
        GPIO.output(lamp.getPgpio(),0)
        GPIO.setup(pinzcr,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
         
    def run(self):
        try:
            while True:
                if GPIO.input(21) == 1:
                    time.sleep(float(lamp.getLumi()))
                    print()
                    print(lamp.getPgpio())
                    GPIO.output(int(lamp.getPgpio()),1)
                    time.sleep(0.000006)
                    GPIO.output(int(lamp.getPgpio()),0)
        except (KeyboardInterrupt):
                print("saindo")

    
           
    
