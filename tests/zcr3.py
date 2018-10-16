#!/usr/bin
# -*- coding: utf-8 -*-
#SCRIPT BY DENIS NASCIMENTO CONCEIÇÃO
#
import RPi.GPIO as GPIO
import time
from decimal import Decimal
#DEFININDO PORTA GPIO NO MODO BROADCOM SOC CHANNEL NUMBER
PIN=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#DEFININDO CONFIGURAÇÕES DOS PINOS
# PINO 21 ZERO CROSSING, 20 ATIVA TRIAC , 15 ATIVA RELE

GPIO.setup(PIN,GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,0)
#GPIO.setup(16,GPIO.OUT)
GPIO.add_event_detect(PIN,GPIO.RISING)
try:
    while True:
        #$if GPIO.event_detected(PIN):
            #t1= Decimal( 8200 * (100 - 50) /100)
        if GPIO.input(PIN) == 1:
              time.sleep(0.00786)
              GPIO.output(20,1)
              time.sleep(0.000006)
              GPIO.output(20,0)
    
except (KeyboardInterrupt):
        print("saindo")
GPIO.cleanup()
exit()
