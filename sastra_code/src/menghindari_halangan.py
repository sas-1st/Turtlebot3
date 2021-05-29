#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    print('===========Cek Halangan============')
    print('s1 [270]')
    print msg.ranges[270]

    print('s2 [0]')
    print msg.ranges[0]

    print('s3 [90]')
    print msg.ranges[90]

    if msg.ranges[0] > 0.5:
	move.linear.x = 0.22
	move.angular.z = 0
    else:
	move.linear.x = 0
	move.angular.z = 0.1
    pub.publish(move)
	
rospy.init_node('menghindari_halangan')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move = Twist()

rospy.spin()
