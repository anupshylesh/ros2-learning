#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed
    
class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.declare_parameter("led_states", [0, 0, 0])
        self.led_states_ = self.get_parameter("led_states").value
        self.led_states_pub_ = self.create_publisher(
            LedStateArray,"led_panel_state",10)
        self.led_pub_timer_ = self.create_timer(5.0,self.publish_led_states)
        self.led_state_service_ = self.create_service(SetLed,"set_led", self.callback_set_led)
        self.get_logger().info("LED panel node has been started")

    def publish_led_states(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_states_pub_.publish(msg)
# here the conditions r mostly for services and 1 for parameter also 
    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):

        if len(request.led_number) != len(request.led_state):    #checks whether the two lists in the service request have the same length.
            response.success = False
            return response

        for led_number, state in zip(request.led_number,request.led_state):
            self.get_logger().info(f"Setting LED {led_number} to {state}")

            if led_number >= len(self.led_states_) or led_number < 0:
                response.success = False
                return response            

            if state not in (0,1):
                response.success = False
                return response
           

            self.led_states_[led_number] = state
        response.success =True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()