#!/usr/bin/env python3
import rospy
from new_pkg.msg import samplemsg  # Assuming your message type is named Samplemsg

def talker():
    pub = rospy.Publisher('chatter', samplemsg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz

    while not rospy.is_shutdown():
        msg = samplemsg()
        msg.id = 1336
        msg.marks = 88.76
        msg.pf = True
        msg.name = "Robotics  %s" % rospy.get_time()
        
        
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
