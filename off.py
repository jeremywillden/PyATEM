#!/usr/bin/env python2.7 
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import config
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(config.gpio_red,   GPIO.OUT)
GPIO.setup(config.gpio_green, GPIO.OUT)

GPIO.output(config.gpio_red,   GPIO.LOW)
GPIO.output(config.gpio_green, GPIO.LOW)
