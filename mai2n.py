import socket
import struct
import RPi.GPIO as GPIO
import pigpio
import time
import subprocess

servo = 13
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo, 50)
print("reset servo")
pwm.set_servo_pulsewidth(servo, 1600);
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
        "-": [9,22]
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




#setup LED lights
GPIO.setup(4, GPIO.OUT) #red
GPIO.setup(27, GPIO.OUT) #green
blinker=True
GPIO.output(27, GPIO.HIGH)


print("getting ip address")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
DIRT_IP = s.getsockname()[0]
DIRT_PORT = 30500
print(DIRT_IP)
s.close()
print("done")

p = subprocess.Popen(['python3', '/home/pi/showip.py', DIRT_IP+"p"+str(DIRT_PORT)])
showingip=True

print("setting dirt rally 2 socket")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((DIRT_IP, DIRT_PORT))
sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,1)
print("socket set!")
print("waiting for data!")


def bit_stream_to_float32(data, pos):
    try:
        value = struct.unpack('f', data[pos:pos+4])[0]
    except struct.error as _:
        value = 0
    except Exception as e:
        value = 0
    return value

def receive(udp_socket):
    global blinker
    global showingip

    if udp_socket is None:
        blinker = True
        return None, None
    try:
        data, addr = udp_socket.recvfrom(1024)  # buffer size is 1024 bytes
    except socket.timeout as _:
        blinker = True
        return None, None
    blinker = False
    if showingip:
        p.terminate()
        showingip = False
    return [bit_stream_to_float32(data, 148),bit_stream_to_float32(data, 132)]


time.sleep(2)
counter=0
try:
    while True:
        result = receive(sock)
        rpm=result[0]
        print(rpm)
        pwm.set_servo_pulsewidth(servo, 1600-int(int(rpm)*1.2875));
        gear=str(result[1])[0]
        overrev = rpm >= 670
        if overrev:
            GPIO.output(4, GPIO.HIGH)
        else:
            GPIO.output(4, GPIO.LOW)
        if blinker:
            GPIO.output(27, GPIO.HIGH)
        else:
            GPIO.output(27, GPIO.LOW)
        displayDigit(gear,overrev)
except KeyboardInterrupt:
    pwm.set_PWM_dutycycle(servo, 0)
    pwm.set_PWM_frequency(servo, 0)
    GPIO.cleanup()