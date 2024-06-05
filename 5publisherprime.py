#!/usr/bin/env python3
import rospy
from new_pkg.msg import samplemsgprime

def publisher_node():
    pub = rospy.Publisher('integer_topic', samplemsgprime, queue_size=10)
    rospy.init_node('integer_publisher_node', anonymous=True)
    #rate = rospy.Rate(10)  # 10Hz
    user_input=int(input("Enter a number:"))

    while not rospy.is_shutdown():
        msg = samplemsgprime()
        msg.user_input = user_input
        pub.publish(msg)


if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass
