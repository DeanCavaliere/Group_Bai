#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import pandas as pd

f = open('data.csv','w')

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twist = Twist()
    twist.angular.x = data.axes[4]  # Left Veritcal Stick
    twist.angular.z = data.axes[0]  # Left Horizontal Stick
    df = pd.DataFrame({'Steering' : [twist.angular.z], 'Speed' : [twist.angular.x]})
    df.to_csv('data.csv',mode='a',header=False,index=False)
    # twist.linear.x = data.axes[4] #Right Vertical Stick
    # twist.angular.z = data.axes[3] #Right Horizontal Stick
    # print(str(Twist))
    # FORWARD/BACK =  1/-1.
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
    # starts the node
    rospy.init_node('VM')
    rospy.spin()


if __name__ == '__main__':
    start()
