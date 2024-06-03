#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def string_length_server():
    rospy.init_node('string_length_server')
    rospy.Subscriber("string_input", String, callback)
    print("Ready to calculate string length and check repeated letter positions.")
    rospy.spin()

def callback(data):
    string_length = len(data.data)
    repeated_positions = {}
    for i, char in enumerate(data.data):
        if data.data.count(char) > 1 and char not in repeated_positions:
            repeated_positions[char] = [i]
        elif data.data.count(char) > 1:
            repeated_positions[char].append(i)

    rospy.loginfo("Received string: %s, Length: %d", data.data, string_length)
    rospy.loginfo("Repeated letter positions:")
    for char, positions in repeated_positions.items():
        rospy.loginfo("%s is present at positions: %s", char, positions)

if __name__ == "__main__":
    string_length_server()

