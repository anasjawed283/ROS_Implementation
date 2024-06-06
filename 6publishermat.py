#!/usr/bin/env python3
import rospy
from new_pkg.msg import matmsg

def talker():
    pub = rospy.Publisher('chatter', matmsg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg=matmsg()
        msg.x=int(input("enter x coordinate: "))
        msg.y=int(input("enter y coordinate: "))
        msg.z=int(input("enter z coordinate: "))
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
