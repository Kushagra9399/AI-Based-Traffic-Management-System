# control_led.py
import requests
import time
import yolo_cam_class

# Replace with the IP address of your Raspberry Pi
raspberry_pi_ip = '192.168.137.119'

# camera here
#cam1 = yolo_cam_class.yolo_cam_class(0)
cam2 = yolo_cam_class.yolo_cam_class('https://192.168.1.6:8080/video')
#cam3 = yolo_cam_class.yolo_cam_class('https://192.168.0.103:8080/video')
#cam4 = yolo_cam_class.yolo_cam_class('https://192.168.0.101:8080/video')
#cam_lst = [cam1,cam2,cam3,cam4]

def send_command(state):
    url = f'http://{raspberry_pi_ip}:6000/led/{state}'
    response = requests.get(url)
    print(response.text)

def send_car(state):
    url = f'http://{raspberry_pi_ip}:6000/car/{state}'
    response = requests.get(url)
    #print(response.text)


if __name__ == '__main__':
    # Example: Turn the LED on
    while True:
        send_command('on')
        #car1 = cam_lst[0].count_car()
        #car2 = cam_lst[1].count_car()
        #car3 = cam_lst[2].count_car()
        #car4 = cam_lst[3].count_car()
        #print(car2)
        #print(car3)
        #print(car4)
        #car2 = 5
        car2 = cam2.count_car()
        car3 = 7
        car4 = 3
        send_car(car2)
        send_car(car3)
        send_car(car4)
        input("Press Enter to turn LED off...")
        send_command('off')