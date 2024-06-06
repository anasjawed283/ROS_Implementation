#!/usr/bin/env python3
import rospy
from new_pkg.msg import sixvalmsg

def talker():
    pub = rospy.Publisher('chatter', sixvalmsg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg=sixvalmsg()
        msg.x=int(input("enter x coordinate: "))
        msg.y=int(input("enter y coordinate: "))
        msg.z=int(input("enter z coordinate: "))
        msg.yaw=int(input("enter yaw |angle about z axis|: "))
        msg.pitch=int(input("enter pitch |angle about y axis|: "))
        msg.roll=int(input("enter roll |angle about x axis|: "))
        msg.distance=int(input("enter distance between flying object and obstacle : "))
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
