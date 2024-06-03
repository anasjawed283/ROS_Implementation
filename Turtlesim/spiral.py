#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist

def spiral():
   rospy.init_node('spiral_node')
   pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
   msg=Twist()
   msg.linear.x=1
   msg.angular.z=2
   rate=rospy.Rate(1)
   spiral_rate=0.5
   
   while not rospy.is_shutdown():
       pub.publish(msg)
       msg.linear.x+=spiral_rate
       rate.sleep()
  
if __name__ == '__main__' :
    try:
        spiral()
    except rospy.ROSInterruptException:
        pass
