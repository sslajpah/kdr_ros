#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

# definicija globalnih spremenljivk
counter = 0
pub = None

# definicija funkcije ob prejetem sporocilu na serverju
def callback_number(msg):
    global counter
    # povecaj stevec za dobljen podatek
    counter += msg.data
    # definicija nove spremenljivke
    new_msg = Int64()
    new_msg.data = counter
    # poslji vrednost vsote
    pub.publish(new_msg)


if __name__ == '__main__':
    
    rospy.init_node('number_counter')
    rospy.loginfo('Counter started.')
    # definicija subscriberja
    sub = rospy.Subscriber("/number", Int64, callback_number)
    # definicija publisherja
    pub = rospy.Publisher("/number_count", Int64, queue_size=10)
    
    # spin zagotovi neskoncni izvajanje zanke
    rospy.spin()
