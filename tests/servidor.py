#!/usr/bin/python
#-*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(14,gpio.OUT)

try:
    val = raw_input("Digite A de ativar ou D desativar")
    if val == 'a':
        gpio.output(14,gpio.HIGH)
    if val == 'd':
        gpio.output(14,gpio.LOW)
#    gpio.cleanup()
except ValueError:
    gpio.cleanup()
