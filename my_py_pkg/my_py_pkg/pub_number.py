#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
    
    
class PublisherNode(Node): 
    def __init__(self):
        super().__init__("number_publisher")
        self.declare_parameter("number",5)
        self.declare_parameter("time_period",1.5)
        self.number_= self.get_parameter("number").value
        self.time_period_= self.get_parameter("time_period").value

        self.number_publisher_ = self.create_publisher(Int64,"number",10)
        self.number_timer_= self.create_timer(self.time_period_,self.publisher_number)
        self.get_logger().info("Started to send number")
        
    def publisher_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)
            
def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()