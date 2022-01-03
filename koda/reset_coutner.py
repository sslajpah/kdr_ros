#!/usr/bin/env python

import rospy
from std_srvs.srv import SetBool

if __name__ == '__main__':
    rospy.init_node('reset_counter')
    # cakaj, dokler ni service na voljo
    rospy.wait_for_service('/reset_number_count')

    try:
        # definicija klienta/ServiceProxy
        reset_cnt = rospy.ServiceProxy('reset_number_count', SetBool)
        # na server poslji prosnjo (True) in pocakaj na povratno informacijo (response)
        response = reset_cnt(True)
        rospy.loginfo('Reset count.')
    except rospy.ServiceException as e:
        # v primeru napake zapisi v log
        rospy.logwarn('Service failed ' + str(e))
