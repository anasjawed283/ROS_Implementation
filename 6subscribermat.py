#!/usr/bin/env python3

import rospy
from new_pkg.msg import matmsg

def callback(data):
    if(data.x>0):
        rospy.loginfo("Moving in X direction %d ",data.x)
    if(data.y>0):
        rospy.loginfo("Moving in y direction %d ",data.y)
    if(data.z>0):
        rospy.loginfo("Moving in z direction %d ",data.z)        
        
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', matmsg, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
