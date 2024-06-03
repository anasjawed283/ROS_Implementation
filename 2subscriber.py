#!/usr/bin/env python3
import rospy
from new_pkg.msg import samplemsg

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' I heard id: %d, name: %s, marks: %f, pass: %s', data.id, data.name, data.marks, data.pf)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', samplemsg, callback)
    rospy.spin()  # Keeps the script from exiting until the node is stopped

if __name__ == '__main__':
    listener()
