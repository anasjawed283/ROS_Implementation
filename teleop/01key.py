#!/usr/bin/env python3
#Anas Jawed 21BRS1336
import rospy
from geometry_msgs.msg import Twist 
import sys, select, termios, tty

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_keyboard_control', anonymous=True)
        self.pub = rospy. Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.twist = Twist()
        
    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_attr)
        return key
        
    def controlLoop(self):
        self.old_attr = termios.tcgetattr(sys.stdin)
        try:
            print("Control the turtle using WASD. Press 'q' to quit.")
            while not rospy.is_shutdown():
                key = self.getKey()
                if key == '1':
                    self.twist.linear.x = 1.0
                elif key == 's':
                    self.twist.linear.x = -1.0
                elif key == '0':
                    self.twist.angular.z = 1.0
                elif key == 'd':
                    self.twist.angular.z = -1.0
                elif key == ' ':
                    self.twist.linear.x = 0.0
                    self.twist. angular.z = 0.0
                elif key == 'q':
                    break
                else:
                    continue
                self.pub.publish(self.twist)
                self.rate.sleep()
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_attr)
        
if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.controlLoop()
    except rospy.ROSInterruptException:
        pass
        
