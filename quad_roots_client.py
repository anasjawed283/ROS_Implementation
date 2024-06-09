#!/usr/bin/env/python3

import rospy
from std_msgs.msg import Float32

if __name__ == '__main__':
 
    rospy.loginfo("client node has started")
    rospy.init_node("client")
 
    rospy.wait_for_service("/quad_roots")

    try:
        quad_roots=rospy.ServiceProxy("/quad_roots", Float32)
        response = quad_roots(1,4,5)llllllll
        rospy.loginfo("Roots are : " + str(response.sum))
    except rospy.ServiceException as e:
        rospy.logwarn("service failed: " + str(e))
