#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):

    print msg.data

rospy.init_node('publisher')
sub = rospy.Subscriber('phrases', String, callback)

rospy.spin()
