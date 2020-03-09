#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import pandas as pd

# This code subscribes to the ROS node 'joy' and then will display
# the corresponding data to screen. It also generates a CSV file 
# called data.csv

# Overwrite / create the csv file 'data.csv'
f = open('data.csv','w')

def callback(data):
    twist = Twist()
    twist.angular.x = data.axes[4]  # Right Veritcal Stick
    twist.angular.z = data.axes[0]  # Left Horizontal Stick
    
    #This code generates a CSV file
    df = pd.DataFrame({'Steering' : [twist.angular.z], 'Speed' : [twist.angular.x]})
    df.to_csv('data.csv',mode='a',header=False,index=False)
    # twist.linear.x = data.axes[4] #Right Vertical Stick
    # twist.angular.z = data.axes[3] #Right Horizontal Stick
    # print(str(Twist))
    
    # Output direction + float value to terminal
    # FORWARD/BACK =  1/-1
    if float(twist.angular.x) > float(0.500):
        hold1 = ('Forwards    ' + str(float(twist.angular.x)) + '           ')
    elif float(twist.angular.x) < float(-0.500):
        hold1 = ('Backwards   ' + str(float(twist.angular.x)) + '           ')
    else:
        hold1 = ('Stop        ' + str(float(twist.angular.x)) + '           ')
        
    # LEFT/RIGHT = 1/-1
    if float(twist.angular.z) > float(0.500):
        hold2 = ('Left        ' + str(float(twist.angular.z)))
    elif float(twist.angular.z) < float(-0.500):
        hold2 = ('Right       ' + str(float(twist.angular.z)))
    else:
        hold2 = ('Straight    ' + str(float(twist.angular.z)))
    print(hold1 + '\t' + hold2)


# Intializes everything
def start():
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node 'VM'
    rospy.init_node('VM')
    rospy.spin()


if __name__ == '__main__':
    start()
