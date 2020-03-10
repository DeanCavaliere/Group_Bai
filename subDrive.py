#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from rpiHAT import ServoNT
import time

# Define Values for Turning
lowTurn = 0.11 # Left
mid = 0.15 # Stop / Straight
highTurn = 0.19 # Right

lowSpeed = 0.14 # Backwards
highSpeed = 0.16 # Forward


def callback(data):
    twist = Twist()
    twist.angular.x = data.axes[4]
    twist.angular.z = data.axes[0]
    #print('linear x is: ' + str(twist.linear.x)) #FORWARD/BACK =  1/-1
    #print('Angular z is ' + str(twist.angular.z)) #LEFT/RIGHT = 1/-1
    
    # Define motor channel 
    s=ServoNT(channel=2, freq=97.9) # Steering
    d=ServoNT(channel=1, freq=97.9) # Driving
    
    if twist.angular.x > float(0.250):
        s.pulse(highSpeed)
    elif (twist.angular.x) < float(-0.250):
        s.pulse(lowSpeed)
    else:
        s.pulse(mid)
        
    # LEFT/RIGHT = 1/-1
    if (twist.angular.z) > float(0.250):
        d.pulse(lowTurn)
    elif (twist.angular.z) < float(-0.250):
        d.pulse(highTurn)
    else:
        d.pulse(mid)

def listener():                                                                                                                                                   # anonymous=True flag means that rospy will choose a unique                                                                                                                                                        # name for our 'listener' node so that multiple listeners can                                                                                                                                                      # run simultaneously.
    rospy.init_node('FastBai')
    rospy.Subscriber('joy', Joy, callback, queue_size=1)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
