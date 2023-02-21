#! /usr/bin/python
import rospy
from std_msgs.msg import String

rospy.init_node('topic_publisher')
pub = rospy.Publisher('phrases', String, queue_size=10) # Here we create the publisher that publishes to the phrases topic

rate = rospy.Rate(2) # Publish at a frequency of 2Hz
msg_str = String()
msg_str = "HELLO WORLD - ROS" # The message

while not rospy.is_shutdown(): # Create a loop 
  pub.publish(msg_str)
  rate.sleep()