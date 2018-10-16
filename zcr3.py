#!/usr/bin
# -*- coding: utf-8 -*-
#SCRIPT BY DENIS NASCIMENTO CONCEIÇÃO
#
import RPi.GPIO as GPIO
import time
import threading
from Lampada import Lampada
from decimal import Decimal
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#DEFININDO PORTA GPIO NO MODO BROADCOM SOC CHANNEL NUMBER
PIN=21
LAMP2=26
PORCENTAGEM=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#DEFININDO CONFIGURAÇÕES DOS PINOS
# PINO 21 ZERO CROSSING, 20 ATIVA TRIAC , 15 ATIVA RELE
GPIO.setup(LAMP2,GPIO.OUT)
GPIO.output(LAMP2,0)
GPIO.setup(PIN,GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,0)
GPIO.setup(16,GPIO.OUT)
GPIO.add_event_detect(PIN,GPIO.RISING)
# METODO MAIN
lamp1 = Lampada("sala",20,0,16,0.0)
lamp2 = Lampada("cozi",26,0,12,0.0)
def main():
    
    #PORCENTAGEM = float(raw_input("DIGITE UM VALOR REAL: "))
    t  = threading.Thread(target=ativaL1(lamp1))
    t2 = threading.Thread(target=ativaL1(lamp2))
#    u = threading.Thread(target=mantemStatus)
#$    u.start()
    t2.start()
    t.start()
    while True:
        try:


            rele = raw_input(" 1 ativa 0 desativa o  rele ou digite c para continuar: ")
            if rele == "c":
                print("proximo passo")
                print("")
            else:
                ativaRele(rele)
            print(lamp.getStatus())
            if lamp.getStatus() == 1:
                 porc = 100 -(float( raw_input("DIGITE UM PORCENTAGEM :")))
                 tempo=(((78.6/100)* float(porc))/10000 )
                 print("")
                 lamp.setLumi(Decimal(tempo))
            time.sleep(1)
        except(KeyboardInterrupt):
            print("acabou")
            GPIO.cleanup()
            exit()
#ATIVA DIMMER TRIAC  LAMPADA
def ativaL1( object):
    lampadas = object
    try:
        
        while True :
            #$if GPIO.event_detected(PIN):
            #t1= Decimal( 8200 * (100 - 50) /100)
            if GPIO.input(PIN) == 1:
            #    print (PORCENTAGEM)
                time.sleep(float(lampadas.getLumi()))
                
                GPIO.output(int(lampadas.getPgpio()),1)
                time.sleep(0.000006)
                GPIO.output(int(lampadas.getPgpio()),0)
    
    except (KeyboardInterrupt):
           print("saindo")

#ATIVA LAMPADA RELE
def ativaRele(liga):
    GPIO.output(int(lamp.getNumRele()),int(liga))
#VERIFICA STATUS D LAMPADA
def mantemStatus():
    comp = lamp.getStatus()
    while True:
        #comp=lamp.getStatus()
        #comp = lamp.getStatus()
        data = mcp.read_adc(1)
        
       # print("lendo do sensor             : " + str( data))
       # print("  ")
        if data > 100:
            status = 1
        else:
            status =0
        if comp != status:
            lamp.setStatus(status)
        time.sleep(1)
        #print(" staus objeto                : " +  str(comp))
    

if __name__ == "__main__":
    main()
