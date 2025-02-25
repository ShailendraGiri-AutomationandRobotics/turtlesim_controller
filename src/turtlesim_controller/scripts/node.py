#!/usr/bin/env python3
import rospy

if __name__== '__main__':
    rospy.init_node('test_node')
    
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo("hello")
        rate.sleep()
