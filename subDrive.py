#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
#from rpiHAT import ServoNT
import time

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    twist = Twist()
    twist.linear.x = data.axes[1]
    twist.angular.z = data.axes[0]
    print('linear x is: ' + str(twist.linear.x)) #FORWARD/BACK =  1/-1
    print('Angular z is ' + str(twist.angular.z)) #LEFT/RIGHT = 1/-1
    #s=ServoNT(channel=2, freq=97.9) #Steering?
    #d=ServoNT(channel=1, freq=97.9) #Driving?
    #s.pulse(dummy)
    #d.pulse(dummy2)
    #.15 center .12 left .17 right


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The                                                                                                                                                           # anonymous=True flag means that rospy will choose a unique                                                                                                                                                        # name for our 'listener' node so that multiple listeners can                                                                                                                                                      # run simultaneously.
    rospy.init_node('FastBai')
    rospy.Subscriber('joy', Joy, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()






