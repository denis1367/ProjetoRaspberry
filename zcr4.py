#!/usr/bin
# -*- coding: utf-8 -*-
#SCRIPT BY DENIS NASCIMENTO CONCEIÇÃO
#
import RPi.GPIO as GPIO
import time
import threading
from Lampada import Lampada
from decimal import Decimal
#DEFININDO PORTA GPIO NO MODO BROADCOM SOC CHANNEL NUMBER
PIN=21
PORCENTAGEM=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#DEFININDO CONFIGURAÇÕES DOS PINOS
# PINO 21 ZERO CROSSING, 20 ATIVA TRIAC , 15 ATIVA RELE

GPIO.setup(PIN,GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,0)
#GPIO.setup(16,GPIO.OUT)
GPIO.add_event_detect(PIN,GPIO.RISING)

# METODO MAIN
lamp = Lampada("sala",20,0,16,0.0)
def main():
    
    #PORCENTAGEM = float(raw_input("DIGITE UM VALOR REAL: "))
    t = threading.Thread(target=ativaL1)
    t.start()
    while True:
        try: 
           # porc = 100 -(float( raw_input("DIGITE UM PORCENTAGEM :")))
           i=0
           while i < 100:
                porc = i              
                tempo=(((78.6/100)* float(porc))/10000 )
               # print(tempo)
              #  print("")
                lamp.setLumi(Decimal(tempo))
                time.sleep(0.03)
                i+=1
        except(KeyboardInterrupt):
            print("acabou")
            GPIO.cleanup()
            exit()

def ativaL1():
    try:
        
        while True :
            #$if GPIO.event_detected(PIN):
            #t1= Decimal( 8200 * (100 - 50) /100)
            if GPIO.input(PIN) == 1:
            #    print (PORCENTAGEM)
                time.sleep(float(lamp.getLumi()))
                
                GPIO.output(int(lamp.getPgpio()),1)
                time.sleep(0.000006)
                GPIO.output(int(lamp.getPgpio()),0)
    
    except (KeyboardInterrupt):
           print("saindo")

if __name__ == "__main__":
    main()
