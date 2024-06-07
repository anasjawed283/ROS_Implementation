#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class PolygonServer:
    def __init__(self):
        rospy.init_node('polygon_server')
        rospy.Subscriber('polygon_info', Int32, self.callback)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(1)
        self.N = 0
        self.T = 0

    def callback(self, data):
        if self.N == 0:
            self.N = data.data
            rospy.loginfo("Received N=%d from client", self.N)
        else:
            self.T = data.data
            rospy.loginfo("Received T=%d from client", self.T)
            self.draw_polygon()

    def draw_polygon(self):
        if self.N <= 2:
            rospy.logwarn("Invalid number of edges. It should be greater than 2.")
            return

        angle = 360.0 / self.N

        twist = Twist()
#        twist.linear.x = self.T
        for _ in range(self.N):
            twist.linear.x = self.T
            twist.angular.z = 0
            self.pub.publish(twist)
            rospy.sleep(1.0)
            
            twist.linear.x = 0
            twist.angular.z = math.radians(angle)
            self.pub.publish(twist)
            rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        polygon_server = PolygonServer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


