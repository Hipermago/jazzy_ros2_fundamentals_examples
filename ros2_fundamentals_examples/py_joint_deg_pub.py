#!/usr/bin/env python3

"""
Description:
This ROS2 node periodically publishes joint angles messages to a topic.

--------------
Publishing topics:
The channel containing the joint angles messages
/joint1_degrees -std_msgs/Float64

Subscription Topics:
None

Author: Alan Hazael
Date:Nov 15 2026
"""

import rclpy #Import The ROS2 client library for python
from rclpy.node import Node #Import the node class, used for creating nodes

from std_msgs.msg import Float64 #Import string message type for 

class JointDegPub(Node):
  """
  Create a joint degree publisher node.
  """
  def __init__(self):
    """
    Create a custom node class for publishing messages
    """
    #Initialize the node with a name
    super().__init__('joint_deg_pub')

    #Create a publisher on the topic with a queue size of 10 messages
    self.publisher_1=self.create_publisher(Float64,'/joint1_degrees',10)

    #Create a timer with a period od .1 seconds to trigger publishing message
    timer_period=1.0
    self.timer = self.create_timer(timer_period,self.timer_callback)

    #initialize a counter variable for degree valueS
    self.i = 0.0

  def timer_callback(self):
    "Callback function executed periodically by the timer"

    #Create a new float message object
    msg=Float64()

    #Set message data with a counter
    msg.data= self.i

    #Publish message you created above to a topic
    self.publisher_1.publish(msg)

    #Log a message indicating the message has been published
    self.get_logger().info(f'Publishing: {msg.data} deg')

    self.i=self.i + 15.0
    if self.i>180.0:
      self.i=0.0

def main(args=None):
  """Main function to start the ROS2 node

  Args:
  args(List,optional): COmmand-line arguments. Default to none
  """

  rclpy.init(args=args)

  #Create an instance of the minimal publisher node
  joint_deg_pub = JointDegPub()
  rclpy.spin(joint_deg_pub)

  #destroy node excplicitly
  joint_deg_pub.destroy_node()

  #Shutdown ROS2 Communication
  rclpy.shutdown()

if __name__=='__main__':
  #Execute the main function if the script is run directly
  main()