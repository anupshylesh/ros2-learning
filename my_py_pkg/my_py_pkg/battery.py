#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
    
    
class BatteryNode(Node): 
    def __init__(self):
        super().__init__("battery")
        self.battery_state = "full"
        self.last_time_battery_state_changed_ = self.get_current_time_seconds()
        self.battery_timer_ = self.create_timer(0.1,self.check_battery_state) 
        self.set_led_client_ = self.create_client(SetLed,"set_led")
        self.get_logger().info("Battery is Started")
    
    def get_current_time_seconds(self):
        seconds, nanoseconds = self.get_clock().now().seconds_nanoseconds()
        return seconds + nanoseconds / 1000000000.0
    

    def check_battery_state (self):
        time_now_ = self.get_current_time_seconds()
        if self.battery_state  == "full":
            if time_now_ - self.last_time_battery_state_changed_> 4.0 :
                self.battery_state = "empty"
                self.get_logger().info("The Battery is empty. Charging mode is ON....." )
                self.call_set_led_client_(2, 1)
                self.last_time_battery_state_changed_ = time_now_
        elif self.battery_state == "empty":
            if time_now_ - self.last_time_battery_state_changed_ > 6.0:
                self.battery_state = "full"
                self.get_logger().info("Battery is full...ready to go")
                self.call_set_led_client_(2, 0)
                self.last_time_battery_state_changed_ = time_now_


    def call_set_led_client_(self, led_number, state):
        while not self.set_led_client_.wait_for_service(1.0):
           self.get_logger().warn("Waiting for Set Led Service....")
        request = SetLed.Request()
        request.led_number = [led_number]
        request.led_state = [state]
        
        future = self.set_led_client_.call_async(request)
        future.add_done_callback(self.callback_call_set_led_client)

    def callback_call_set_led_client(self,future):
        response: SetLed.Response = future.result()
        if response.success:
            self.get_logger().info("Led State is changed")
        else:
            self.get_logger().info("Led state not changed")

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode() 
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()