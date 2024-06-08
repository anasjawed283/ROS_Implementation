#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def string_length_client():
    rospy.init_node('string_length_client')
    pub = rospy.Publisher("string_input", String, queue_size=10)
    rospy.sleep(1)  # wait for publisher to set up
    input_str = input("Enter a string: ")  # For Python 3
    rospy.loginfo("Sending string: %s", input_str)
    pub.publish(input_str)

if __name__ == "__main__":
    string_length_client()

