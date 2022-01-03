#!/usr/bin/env python

# vkljucitev python ros knjiznice
import rospy


if __name__ == '__main__':
    # inicializacija node
    rospy.init_node('my_first_python_node')
    # zapis v log
    rospy.loginfo('This node has been started.')
    # pocakaj 1 sekundo
    rospy.sleep(1)
    # izhod
    print('Exit now')