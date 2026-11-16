#!/usr/bin/env python3

"""
Description:
This ROS2 node subscribes to joint degree messages
------------------------------------------------------
Publishing topics:
NONE
------------------------------------------------------
Subscription TOPIC
The channel containing the hello world messages
/joint1_degrees -std_msgs/Float64
------------------------------------------------------

Author:
ALan Hidrogo

Date: NOV 15 2026
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64 #Import string message type for 
import math

class JointDegSub(Node):
    def __init__(self):
        super().__init__('joint_deg_sub')

        self.subscriber_1=self.create_subscription(
            Float64,
            '/joint1_degrees',
            self.listener_callback,
            10)

    def listener_callback(self,msg):
        rad=math.radians (msg.data)
        self.get_logger().info(f'I heard: {rad}')

def main(args=None):
    rclpy.init(args=args)
    joint_deg_sub=JointDegSub()
    rclpy.spin(joint_deg_sub)
    
    joint_deg_sub.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
