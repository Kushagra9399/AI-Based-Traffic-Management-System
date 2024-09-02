import time
from gpiozero import LED

class led:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    led1 = LED(a)
    led2 = LED(b)
    led3 = LED(c)
    led4 = LED(d)
    def on(a):
        if a==1:
            led1.on()
            led2.off()
            led3.off()
            led4.off()
        elif a==2:
            led1.off()
            led2.on()
            led3.off()
            led4.off()
        elif a==3:
            led1.off()
            led2.off()
            led3.on()
            led4.off()
        elif a==4:
            led1.off()
            led2.off()
            led3.off()
            led4.on()
        elif a==0:
            led1.off()
            led2.off()
            led3.off()
            led4.off()
        else:
            print("Wrong input...")
