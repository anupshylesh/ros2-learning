#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
    
    
class MyProject1(Node): 
    def __init__(self):
        super().__init__("pub_counter")
        self.publishers_ = self.create_publisher(Int64,"counter",10)
        self.count_ = 1
        self.timer_ = self.create_timer(1.0,self.callback_publish_number)

    def callback_publish_number(self):
        msg =Int64()
        msg.data = self.count_
        self.publishers_.publish(msg)
        self.get_logger().info(f"Publishing: {self.count_}")
        self.count_ +=1

    
    
def main(args=None):
    rclpy.init(args=args)
    node = MyProject1() 
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()