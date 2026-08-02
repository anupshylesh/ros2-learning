#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
    
    
class MyProject1(Node): 
    def __init__(self):
        super().__init__("sub_counter")
        self.subscriber_ = self.create_subscription(Int64,"counter",self.callback_counter,10)
        self.get_logger().info("Ready to receive numbers")
        self.total_ = 0
        self.avg_ = 0
        self.count_received_ = 0
        self.threshold_value_ = 10
        self.threshold_total_ = 100

    def callback_counter(self,msg):
        self.count_received_+= 1
        self.total_ += msg.data
        self.avg_ = self.total_/ self.count_received_
        self.get_logger().info(
            f"Received Number: {msg.data} | Total Number: {
                self.total_} | Average Number: {self.avg_}")
        if msg.data > self.threshold_value_:
            self.get_logger().error("Receive data is crossed the threshold value")
        if self.total_ > self.threshold_total_:
            self.get_logger().error("Receive data's sum value crossed the threshold total value")
        
       
    
    
def main(args=None):
    rclpy.init(args=args)
    node = MyProject1()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()