import time
import led_class
# red, green, yellow, blue
lane1 = led(17,27,10,7) 
lane2 = led(17,27,10,7)
lane3 = led(17,27,10,7)
lane4 = led(17,2,10,7)

total_time_max = 400
total_time_min = 120
time_min = 5
time_max = 100
time_lap = 60
car1 = 10
car2 = 20
car3 = 5
car4 = 15
while True:
    lane1.on(2)
    #lane1 green on
    total_car = car1+car2+car3+car4
    if total_car >= 60:
        time_lap = total_time_max/total_car
    else:
        time_lap = total_time_min/total_car
    lane1_time = time_lap*car1
    lane2_time = time_lap*car2
    lane3_time = time_lap*car3
    lane4_time = time_lap*car4
    while lane1.on():
        time.sleep(2)
        #lane1 red on
        lane1.on(0)
        lane2.on()
    while lane2.on():
        time.sleep(2)
        lane2.on(0)
        lane3.on()
    while lane3.on():
        time.sleep(2)
        lane3.on(0)
        lane4.on()
    while lane4.on():
        time.sleep(2)
        lane4.on(0)
        lane1.on()
        
