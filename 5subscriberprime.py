#!/usr/bin/env python3
import rospy
from new_pkg.msg import samplemsgprime

def isprime(number):
    if number <=1:
       return False
    for i in range(2, int(number**0.5)+1):
       if (number % i==0):
          return False
    return True
    
def callback(data):
    if isprime(data.user_input):
       rospy.loginfo("PRIME")
    else:
       rospy.loginfo("NOT PRIME")

def subscriber_node():
    rospy.init_node('integer_subscriber_node', anonymous=True)
    rospy.Subscriber('integer_topic', samplemsgprime, callback)
    rospy.spin()  # Keeps the script from exiting until the node is stopped

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass
