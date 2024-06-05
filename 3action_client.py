#!/usr/bin/env python3

import rospy
import actionlib
import actionlib_tutorials.msg

def fibonacci_client():
    rospy.init_node('fibonacci_client')
    

    client = actionlib.SimpleActionClient('fibonacci', actionlib_tutorials.msg.FibonacciAction)
    client.wait_for_server()
    
    goal = actionlib_tutorials.msg.FibonacciGoal(order=10)
    
    client.send_goal(goal)
    
    client.wait_for_result()
    
    result = client.get_result()
    print("Fibonacci sequence:", result.sequence)

if __name__ == '__main__':
    fibonacci_client()
