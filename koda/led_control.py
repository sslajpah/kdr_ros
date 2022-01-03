#!/usr/bin/env python

import rospy
# vkljucitev sporocila iz lastne knjiznice
from kdr_msgs.srv import SetLed

# definicja funkcije za komunikacijo s serverjem
def set_led(ledNum):
    # cakaj, dokler server ni na voljo
    rospy.wait_for_service("/set_led")
    try:
        # definicija klienta
        service = rospy.ServiceProxy("/set_led", SetLed)
        # definicija zahteve in odziva
        resp = service(ledNum)
        rospy.loginfo("Set led success flag : " + str(resp))
    except rospy.ServiceException as e:
        rospy.logerr('Service failed ' + str(e))

if __name__ == '__main__':
    rospy.init_node('led_controller')
    
    while not rospy.is_shutdown():
        # sekvencno prizigaj po eno led
        for led_num in range(5):
            print(led_num)
            set_led(led_num)
            rospy.sleep(0.1)