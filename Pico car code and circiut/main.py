# Pico Car

from machine import Pin,PWM
from time import sleep

PWMA = PWM(Pin(8))
AIN2 = Pin(9, Pin.OUT)
AIN1 = Pin(10, Pin.OUT)

PWMB = PWM(Pin(13))
BIN2 = Pin(12, Pin.OUT)
BIN1 = Pin(11, Pin.OUT)

SensorL = Pin(27, Pin.IN)
SensorR = Pin(26, Pin.IN)

def Control( SpeedL, SpeedR, A1HL, A2HL, B1HL, B2HL):

    PWMA.duty_u16(SpeedL) # 50000, Max = 65535
    AIN1.value(A1HL)
    AIN2.value(A2HL)
 
    PWMB.duty_u16(SpeedR)
    BIN1.value(B1HL)
    BIN2.value(A2HL)


while True:
    if (not SensorL.value() == 1 and  not SensorR.value() == 1):
        
        Control(50000, 50000, 1, 0, 1, 0)

    elif ( SensorL.value() == 1 and not SensorR.value() == 1):

        Control(50000, 35000, 0, 1, 1, 0)

    elif ( not SensorL.value() == 1 and  SensorR.value() == 1 ):

        Control(35000, 50000, 1, 0, 0, 1)

    else: 

        Control(0, 0, 0, 0, 0, 0)


