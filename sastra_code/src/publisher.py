#! /usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('publisher')
pub = rospy.Publisher('phrases', String, queue_size=10)

rate = rospy.Rate(2)
msg_str = String()
msg_str = "Hello my bro, comeback with me Sastra"

while not rospy.is_shutdown():
   print(msg_str) 
   pub.publish(msg_str)
   rate.sleep()
