# led_control.py
import time
from flask import Flask, request
import led_class

app = Flask(__name__)

def change_lane(a):
    a[0],a[1],a[2],a[3]=a[3],a[0],a[1],a[2]
    return a

def led_run():
    lanes[2].off()
    time.sleep(0.5)
    lanes[3].off()
    time.sleep(0.5)

    #timer1 = timer.Timer(time_lane2)

    lanes[1].on(1)
    time.sleep(0.5)
    lanes[0].on(1)
    time.sleep(1)
    lanes[1].off()
    lanes[0].on()
    time.sleep(2)
    car2 = 5
    car3 = 10
    car4 = 6
    total_car = car2 + car3 + car4
    if total_car>30:
       time_per_lane = time_max//total_car
    elif total_car == 0:
        time_per_lane = 1
    else:
        time_per_lane = time_min//total_car
    #time_lane1 = time_per_lane*car1
    time_lane2 = max(time_per_lane*car2,5)
    time_lane3 = max(time_per_lane*car3,5)
    time_lane4 = max(time_per_lane*car4,5)
    #change_cam(cam_lst)
    print(time_lane2)
    change_lane(lanes)
    return "complete"

# GPIO setup
lane1 = led_class.LEDController(2,3,4,17)
lane2 = led_class.LEDController(27,22,23,24)
lane3 = led_class.LEDController(25,8,7,11)
lane4 = led_class.LEDController(19,26,16,20)
lanes = [lane1,lane2,lane3,lane4]

time_max = 400
time_min = 120
time_lane2 = 15

lanes[1].on()
lanes[0].off()
lanes[2].off()
lanes[3].off()
#time.sleep(1)

# main code below (don't touch it...) very important
@app.route('/led/<state>', methods=['GET'])
def control_led(state):
    if state == 'on':
        return led_run()

    elif state == 'off':
        #led1.off()
        return "LED is OFF"
    else:
        return "Invalid state. Use 'on' or 'off'."

@app.route('/car/<state>',methods=['GET'])
def car_iden(state):
    print(state)
    return "Car taken"

@app.route('/amb/<state>',methods=['GET'])
def amb_iden(state):
    print(state)
    return "Ambulance Detected"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
