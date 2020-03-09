#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from rpiHAT import ServoNT
import time

lowTurn = 0.11
mid = 0.15
highTurn = 0.19

lowSpeed = 0.14
highSpeed = 0.16


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    twist = Twist()
    twist.angular.x = data.axes[4]
    twist.angular.z = data.axes[0]
    #print('linear x is: ' + str(twist.linear.x)) #FORWARD/BACK =  1/-1
    #print('Angular z is ' + str(twist.angular.z)) #LEFT/RIGHT = 1/-1
    s=ServoNT(channel=2, freq=97.9) #Steering?
    d=ServoNT(channel=1, freq=97.9) #Driving?
    if twist.angular.x > float(0.250):
       # hold1 = (float(twist.linear.x)) #Forwards
        s.pulse(highSpeed)
    elif (twist.angular.x) < float(-0.250):
       # hold1 = (float(twist.linear.x)) #Backwards
        s.pulse(lowSpeed)
    else:
        #hold1 = (float(twist.linear.x)) #STOP
        s.pulse(mid)
    # LEFT/RIGHT = 1/-1
    if (twist.angular.z) > float(0.250):
       # hold2 = (float(twist.angular.z)) #LEFT
        d.pulse(lowTurn)
    elif (twist.angular.z) < float(-0.250):
       # hold2 = (float(twist.angular.z)) #RIGHT
        d.pulse(highTurn)
    else:
       #hold2 = (float(twist.angular.z)) #STRAGHT
        d.pulse(mid)
        #print()
    #d.pulse(dummy2)
    #.15 center .12 left .17 right


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The                                                                                                                                                           # anonymous=True flag means that rospy will choose a unique                                                                                                                                                        # name for our 'listener' node so that multiple listeners can                                                                                                                                                      # run simultaneously.
    rospy.init_node('FastBai')
    rospy.Subscriber('joy', Joy, callback, queue_size=2)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()






