#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
# vkljucitev service sporocila iz std_srvs
from std_srvs.srv import SetBool

counter = 0
pub = None

def callback_number(msg):
    global counter
    counter += msg.data
    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)

# definicija funkcije za reset stevca
def callback_reset_counter(req):
    # req.data je lahko true/false
    if req.data:
        global counter
        counter = 0
        # povratno sporocilo ima dve polji: success in message
        # return {'success':True, 'message':'TEXT'}
        return True, "Counter has been successfully reset"
    return False, "Counter has not been reset"

if __name__ == '__main__':
    
    rospy.init_node('number_counter')
    rospy.loginfo('Counter started.')
    
    sub = rospy.Subscriber("/number", Int64, callback_number)
    
    pub = rospy.Publisher("/number_count", Int64, queue_size=10)
    # definicija service z ustreznim klicem callback funkcije
    reset_service = rospy.Service("/reset_number_count", SetBool, callback_reset_counter)
    
    rospy.spin()
