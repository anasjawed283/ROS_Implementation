#!/usr/bin/env python3
#Anas Jawed 21BRS1336
import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('turtle_controller', anonymous=True)
    pub = rospy. Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate (10) # 10 Hz
    twist = Twist()
    
    while not rospy.is_shutdown():
        move_command = int(input("Enter 1 to move turtle or to stop: ")) # Take input inside the loop
        if move_command == 1:
            twist.linear.x = 2 # move forward with a linear velocity of 2 m/s
            twist.angular.z = 0.0 # no angular velocity
            pub.publish(twist) # Publish the twist message
        elif move_command == 0:
                twist.linear.x = 0.0 # stop linear motion
                twist.angular.z = 0.0 # stop angular motion
                pub.publish(twist) # Publish the twist message
        else:
            rospy.logwarn("Invalid input. Please enter either or 1.")
            continue # Skip publishing if the input is invalid
            
        rate.sleep() # Sleep to maintain the publishing rate

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
