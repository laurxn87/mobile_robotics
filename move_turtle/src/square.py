# #! /usr/bin/env python
# import rospy
# from geometry_msgs.msg import Twist, Point

# def mover():
# rospy.init_node('vel_publisher')
# rospy.loginfo("Press Ctrl + C to terminate")
# pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
# pub2 = rospy.Publisher('cmd_vel', Pose, queue_size=10)
# move = Twist()
# place = Point()

# # Publish at the rate of 1Hz
# rate = rospy.Rate(1)
# while not rospy.is_shutdown():
#     # Set the velocity here: using Twist.linear.x/y/z and/or Twist.angular.x/y/z 
#     # TODO 
#     if place.x == 0 and place.y == 0:
#         move.linear.x = 1
#     if place.x == 4 and place.y == 0:
#         move.angular = 1/4
#         move.linear.x = 1
#     if place.x == 4 and place.y == 4:
#         move.angular = 1/4
#         move.linear.x = 1
#     if place.x == 0 and place.y == 4:
#         move.angular = 1/4
#         move.linear.x = 1
            
#     pub.publish(move)
#     rate.sleep()

# if __name__ == '__main__':
# try:
#     mover()
# except rospy.ROSInternalException:
#     rospy.loginfo("Action terminated.")

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pi

class Turtlebot3():
    def __init__(self):
        rospy.init_node("turtlebot3_move_square")
        rospy.loginfo("Press Ctrl + C to terminate")
        self.vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.run()


    def run(self):
        vel = Twist()
        vel.linear.x = 0.5
        vel.angular.z = 0
        #while not rospy.is_shutdown():  # uncomment to use while loop
        for i in range(50):
            self.vel_pub.publish(vel)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        robot = Turtlebot3()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action terminated.")