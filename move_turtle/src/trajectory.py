#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def mover():
rospy.init_node('vel_publisher')
rospy.loginfo("Press Ctrl + C to terminate")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
move = Twist()

# Publish at the rate of 1Hz
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    # Set the velocity here: using Twist.linear.x/y/z and/or Twist.angular.x/y/z 
    # TODO
            
    pub.publish(move)
    rate.sleep()

if __name__ == '__main__':
try:
    mover()
except rospy.ROSInternalException:
    rospy.loginfo("Action terminated.")