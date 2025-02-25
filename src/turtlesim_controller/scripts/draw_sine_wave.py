#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
import math

if __name__ == '__main__':
    rospy.init_node('sine_wave')
    rospy.loginfo("Node has started")

    #rospy.wait_for_service('/clear')  # Wait for the clear service to be available
    clear_service = rospy.ServiceProxy('/clear', Empty)  # Create a service proxy
    clear_service()  # Call the service to clear the canvas

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)
    amplitude = 2.0
    frequency = 0.5

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 1.0

        current_time = rospy.get_time()
        msg.angular.z = amplitude*math.sin(frequency*current_time)
        
        pub.publish(msg)
        rate.sleep()