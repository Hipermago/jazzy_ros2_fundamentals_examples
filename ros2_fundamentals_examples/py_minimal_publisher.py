#!/usr/bin/env python3

"""
Description:
This ROS2 node periodically publishes "hello world" messages to a topic.

--------------
Publishing topics:
The channel containing the "Hello world" messages
/py_example_topic -std_msgs/String

Subscription Topics:
None

Author: Alan Hazael
Date:Nov 14 2026
"""

import rclpy #Import The ROS2 client library for python
from rclpy.node import Node #Import the node class, used for creating nodes

from std_msgs.msg import String #Import string message type for 

class MinimalPyPublisher(Node):
  """
  Create a minimal publisher node.
  """
  def __init__(self):
    """
    Create a custom node class for publishing messages
    """
    #Initialize the node with a name
    super().__init__('minimal_py_publisher')

    #Create a publisher on the topic with a queue size of 10 messages
    self.publisher_1=self.create_publisher(String,'/py_example_topic',10)

    #Create a timer with a period od .5 seconds to trigger publishing message
    timer_period=0.5
    self.timer = self.create_timer(timer_period,self.timer_callback)

    #initialize a counter variable for message content
    self.i = 0

  def timer_callback(self):
    "Callback function executed periodically by the timer"

    #Create a new string message object
    msg=String()

    #Set message data with a counter
    msg.data= 'Hello World: %d' % self.i

    #Publish message you created above to a topic
    self.publisher_1.publish(msg)

    #Log a message indicating the message has been published
    self.get_logger().info('PUblishing:"%s"'%msg.data)
    self.i=self.i + 1

def main(args=None):
  """Main function to start the ROS2 node

  Args:
  args(List,optional): COmmand-line arguments. Default to none
  """

  rclpy.init(args=args)

  #Create an instance of the minimal publisher node
  minimal_py_publisher = MinimalPyPublisher()
  rclpy.spin(minimal_py_publisher)

  #destroy node excplicitly
  minimal_py_publisher.destroy_node()

  #Shutdown ROS2 Communication
  rclpy.shutdown()

if __name__=='__main__':
  #Execute the main function if the script is run directly
  main()