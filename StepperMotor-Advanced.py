from machine import Pin
import time
IN1 = Pin(5,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(18,Pin.OUT)
IN4 = Pin(19,Pin.OUT)
List1= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
List2= [IN1,IN2,IN3,IN4]
while True:
    for i in List1:
        for j in range(4):
            List2[j].value(i[j])
        time.sleep_ms(2)
