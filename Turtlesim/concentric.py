#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from math import pi

def draw_circle(radius):
    rospy.init_node('concentric_circles')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  
    twist = Twist()
    twist.linear.x = 2.0
    twist.angular.z = twist.linear.x / radius
    circle_time = 2 * pi * radius / twist.linear.x
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < 2*circle_time:
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    twist.angular.z = pi+pi/2  
    pub.publish(twist)
    rospy.sleep(1)  
    twist.angular.z = 0.0
    pub.publish(twist)
    twist.linear.x = 1   
    pub.publish(twist)
    rospy.sleep(1)  
    twist.linear.x = 0.0
    pub.publish(twist)
    twist.angular.z = -pi-pi/2  
    pub.publish(twist)
    rospy.sleep(1)  
    twist.angular.z = 0.0
    pub.publish(twist)
    twist.linear.x = 2.0
    twist.angular.z = twist.linear.x / (radius+1)
    circle_time = 2 * pi * (radius+1) / twist.linear.x
    start_time = rospy.Time.now().to_sec() 
    while rospy.Time.now().to_sec() - start_time < circle_time:
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    twist.angular.z = pi+pi/2  
    pub.publish(twist)
    rospy.sleep(1)  
    twist.angular.z = 0.0
    pub.publish(twist)
    twist.linear.x = 1   
    pub.publish(twist)
    rospy.sleep(1)  
    twist.linear.x = 0.0
    pub.publish(twist)
    twist.angular.z = -pi-pi/2  
    pub.publish(twist)
    rospy.sleep(1)  
    twist.angular.z = 0.0
    pub.publish(twist)
    twist.linear.x = 2.0
    twist.angular.z = twist.linear.x / (radius+2)
    circle_time = 2 * pi * (radius+2) / twist.linear.x
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < circle_time:
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)    
    
if __name__ == '__main__':
    try:
        draw_circle(1)  
    except rospy.ROSInterruptException:
        pass
