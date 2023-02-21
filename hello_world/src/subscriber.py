#! /usr/bin/python
import rospy
from std_msgs.msg import String

def callback(msg): # A callback function to print the msg
  print msg.data

rospy.init_node('topic_subscriber') 
sub = rospy.Subscriber('/phrases',String, callback) # Create a subscriber

rospy.spin() # Create a loop