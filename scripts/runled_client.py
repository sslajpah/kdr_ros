#!/usr/bin/env python

import rospy
import actionlib
# import action server messages
from kdr_msgs.msg import runningLedAction, runningLedGoal, runningLedResult

# define action server status
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

client = None

def run_led_client(goalNum):
    global client
    # Creates the SimpleActionClient, 
    client = actionlib.SimpleActionClient('run_led', runningLedAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = runningLedGoal()
    goal.numberOfRuns = goalNum

    # Sends the goal to the action server.
    client.send_goal(goal)

    
    """####################
    # Test new goal - old goal is canceled after 3 seconds
    rospy.sleep(3)
    goal.numberOfRuns = 2
    client.send_goal(goal)
    #####################"""
    
    # Case A) Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()
    
    """
    #########################################3
    # Case B: let us do some other stuff
    current_state = client.get_state()

    while_rate = rospy.Rate(1)
    
    # check for change in state
    while current_state < DONE:
        # action is still active, let us do something
        current_state = client.get_state()
        print(current_state)
        while_rate.sleep()

    # server is DONE, result is returned
    final_res = client.get_result()
    print("[Result] Result is "+str(final_res))
    
    if current_state == WARN:
        rospy.logwarn("[Warn] Warning on the action server side.")

    if current_state == ERROR:
        rospy.logerr("[Error] Error on the action server side.")

    return final_res
    #########################################3
    """


if __name__ == '__main__':
    rospy.init_node('run_led_client')
    
    try:
        # call action server client, wait for result
        result = run_led_client(goalNum = 10)
        #result = run_led_client(goalNum = rospy.get_param('/number_of_runs'))
        print("Result: %i" % result.finalRun)
        
    except rospy.ROSInterruptException:
        print("Program interrupted before completion.")
