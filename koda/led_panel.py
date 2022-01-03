#!/usr/bin/env python

import rospy
# vkljucitev sporocila iz lastne knjiznice
from kdr_msgs.srv import SetLed

# definicija globalne spremenjivke
led_states = list('-----')


# definicija funkcije za prizig ustrezne led
def callback_set_led(req):
    global led_states

    led_states = list('-----')
    # dobi stevilko led iz zahtevka
    led_number = req.LedNumber
    
    # ce je zahtevek nesmiseln, prekini izvanje vrni napako
    if (led_number > len(led_states)) or (led_number < 0):
        return {'success': False, 'message':'Wrong LED number.'}
    
    
    # prizgi ustrezno led
    led_states[led_number] = 'O'
    
    return {'success': True, 'message':'Successfully turned on LED '+str(led_number)+'.'}

if __name__ == '__main__':
    
    rospy.init_node('led_panel')
    
    # definicija serverja
    server = rospy.Service("/set_led", SetLed, callback_set_led)
    
    rate = rospy.Rate(10)
    
    # izpisuj led matriko
    while not rospy.is_shutdown():
        print("".join(led_states))
        rate.sleep()

