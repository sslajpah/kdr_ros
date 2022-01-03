#!/usr/bin/env python

import rospy
import actionlib
# import action server messages
from kdr_msgs.msg import runningLedFeedback, runningLedResult, runningLedAction

ACserver = None

led_states = list('-----')

# callback function to complete goal 
def goal_callback(goal):

    # define feedback
    feedback1 = runningLedFeedback()
    # define result
    result1 = runningLedResult()

    # Do lots of awesome groundbreaking robot stuff here
    print("Awesome stuff going on.")    
    print("Stevilo iteracij: %i" % goal.numberOfRuns)
    
    r = rospy.Rate(4)
    #r = rospy.Rate(rospy.get_param('/led_frequency'))
    
    success = True
    doPreemt = False

    for kk in range(1,goal.numberOfRuns+1):
        for led_number in range(5):
            # check for preempt before every LED change
            if ACserver.is_preempt_requested():
                print('Preempted. New goal received.')
                result1.finalRun = kk
                # set goal status as preemted (does not work with simple action server)
                ACserver.set_preempted(result=result1,text='New goal received!')
                success = False 
                doPreemt = True
                # stop for loop - led_number
                break
            
            
            # this is that goundbreaking robotic stuff
            led_states = list('-----')
            led_states[led_number] = 'O'
            print("".join(led_states))
            r.sleep()
        
        if doPreemt:
            # stop for loop - kk
            break
        # publish the feedback
        feedback1.currentRun = kk
        print('Feedback send.')
        ACserver.publish_feedback(feedback1)

    # publish the result
    if success:
        result1.finalRun = feedback1.currentRun
        rospy.loginfo('Finished successfully.') 
        # set goal status to succeeded  - does not work with simple action server
        ACserver.set_succeeded(result1)


if __name__ == '__main__':
    rospy.init_node('run_led_server')
    # simple action server definition
    ACserver = actionlib.SimpleActionServer('run_led', runningLedAction, goal_callback, False)

    # start server
    ACserver.start()
    print('Action server running')

    rospy.spin()