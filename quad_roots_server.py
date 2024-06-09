#!/usr/bin/env python3

import rospy
import cmath
from std_msgs.msg import Float32
import re


def compute_roots(req):
    result = req.a + req.b + req.c
    rospy.loginfo("sum of " + str(req.a) + " and " + str(req.b) + " is " + str(result))
    return result
    
if __name__ == '__main__':
    rospy.init_node("server")
    rospy.loginfo("server node has started")

    service=rospy.Service("/quad_roots", Float32, compute_roots)
    rospy.loginfo("service server has been started")
    
    rospy.spin()
