#!/usr/bin/env python3

import rospy
from new_pkg.msg import sixvalmsg

def callback(data):
    if(data.x>0):
        rospy.loginfo("Moving in X direction %d ",data.x)
    if(data.y>0):
        rospy.loginfo("Moving in y direction %d ",data.y)
    if(data.z>0):
        rospy.loginfo("Moving in z direction %d ",data.z) 
    if(data.yaw>0):
        rospy.loginfo("Angular change about z axis %d ",data.yaw)
    if(data.pitch>0):
        rospy.loginfo("Angular change about y axis %d ",data.pitch)
    if(data.roll>0):
        rospy.loginfo("Angular change about x axis %d ",data.roll) 
    if(data.distance>0):
        rospy.loginfo("Aistance between flying object and obstacle %d ",data.distance)      
        
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', sixvalmsg, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
