import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
# _       24
#|_|   23 22 25
#|_| . 9  10 11 18
#
#setup LED display
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def resetDigits():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)

resetDigits()

def displayDigit(digit,dot):
    digits = {
        "0": [24,23,25,9,10,11],
        "1": [25,11],
        "2": [24,22,25,9,10],
        "3": [24,22,25,10,11],
        "4": [23,22,25,11],
        "5": [24,23,22,10,11],
        "6": [24,23,22,9,10,11],
        "7": [24,25,11],
        "8": [24,23,22,25,9,10,11],
        "9": [24,23,22,25,10,11],
        "p": [24,23,22,25,9]
    }
    if dot:
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    for pin in digits[digit]:
        GPIO.output(pin, GPIO.HIGH)

counter=0
DIRT_IP = sys.argv[1]
while True:
    time.sleep(1)
    if DIRT_IP[counter] == ".":
        counter+=1
    try:
        displayDigit(DIRT_IP[counter],DIRT_IP[counter+1]==".")
    except IndexError:
        displayDigit(DIRT_IP[counter], False)
    print(counter)
    if counter<len(DIRT_IP)-1:
        counter+=1
    else:
        time.sleep(1)
        resetDigits()
        counter=0