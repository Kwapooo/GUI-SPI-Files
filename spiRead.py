#!/usr/bin/python3

# --------------------------------------- #
# Program Author:
# Date of Creation: 06/22/22
# Last Modified: 07/07/22
# Function: Display Voltage Data to Console
# Comments: Test Program
# ---------------------------------------- #

import time
import spidev
import RPi.GPIO as GPIO

# Hide any warning in console
GPIO.setwarnings(False)

# Setting up SPI reading
GPIO.setmode(GPIO.BCM)

# Opening the SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# Chip Select
CS_ADC = 12
GPIO.setup(CS_ADC, GPIO.OUT)


# Channel Select
def readChannel3208(channel):

	adc = spi.xfer2([6 | (channel >> 2), channel << 6, 0])
	data = ((adc[1] & 15) << 8) + adc[2]
	return data


def convertToVoltage(value, bitCount, vRef):
	return vRef * (value / (2 ** bitCount - 1))


# Conditional loop that will print voltage data
i = 0

# 'i' will be unchanged so the loop runs infinitely
while i == 0:

	GPIO.output(CS_ADC, GPIO.LOW)
	value = readChannel3208(1)
	GPIO.output(CS_ADC, GPIO.HIGH)
	global voltage
	voltage = convertToVoltage(value, 12, 3.3)

	# print(f"{voltage:.3f}")

	# Delay time between readings (1 unit = 1 second)
	delayTime = 0.125
	time.sleep(delayTime)
