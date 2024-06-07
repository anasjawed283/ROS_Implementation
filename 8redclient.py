#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def polygon_client():
    rospy.init_node('polygon_client', anonymous=True)
    pub = rospy.Publisher('polygon_info', Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    N = int(input("Enter the number of edges (N): "))
    T = int(input("Enter the edge length (T): "))

    while not rospy.is_shutdown():
        pub.publish(N)
        rospy.loginfo("Sending N=%d to server", N)
        rospy.sleep(1.0)
        pub.publish(T)
        rospy.loginfo("Sending T=%d to server", T)
        rospy.sleep(1.0)
        break

if __name__ == '__main__':
    try:
        polygon_client()
    except rospy.ROSInterruptException:
        pass
