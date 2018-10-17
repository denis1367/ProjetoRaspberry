#!/usr/bin
# -*- coding: utf-8 -*-
#
import RPi.GPIO as GPIO
import time
import threading


#GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)

class PortaGpio(object):
    def __init__(self,porta,pinzcr):
        self.GPIO.setup(porta,GPIO.OUT)
        self.GPIO.output(porta,0)
    def ativaTriac(object):
        lampadas = object
        try:
            
            while True:
                if GPIO.input(pinzcr) ==1:
                    time.sleep(float(lampadas.getLumi()))
                    GPIO.output(int(lampadas.getPgpio()),1)
                    time.sleep(0.000006)
                    GPIO.output(int(lampadas.getPgpio()),0)
        except (KeyboardInterrupt):
            print(" erro na class PortasGpio")

    
