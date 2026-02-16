from machine import Pin
import time
IN1 = Pin(5,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(18,Pin.OUT)
IN4 = Pin(19,Pin.OUT)
List1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
List1rev = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
while True:
    for i in range(500):
        for j in List1:
            IN1.value(i[0])
            IN1.value(i[1])
            IN1.value(i[2])
            IN1.value(i[3])
            time.sleep_ms(5)

    for i in range(500):
        for k in List1rev:
            IN1.value(i[0])
            IN1.value(i[1])
            IN1.value(i[2])
            IN1.value(i[3])
            time.sleep_ms(5)
