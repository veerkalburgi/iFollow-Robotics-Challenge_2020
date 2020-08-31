		# -*- coding: utf-8 -*-
# with known parameters wheel radious and robot footprint
import numpy as np
import rospy
import roslib
import subprocess
import time
from geometry_msgs.msg  import Twist
from sensor_msgs.msg import Joy
import sys
import signal

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
''' class '''
class robot():
    def __init__(self):
        rospy.init_node('robot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.pose_subscriber2 = rospy.Subscriber('/joy',Joy,self.callback)
        self.rate = rospy.Rate(20)

    def callback(self, data):
        global inn
        inn=0
        self.joy = data.buttons
        self.joy2= data.axes
        if np.shape(self.joy)[0]>0:
            inn=1
            self.nemo=self.joy[0]
            self.semo=self.joy[3]
            self.one=self.joy[2]
            self.x=self.joy[1]
        if np.shape(self.joy2)[0]>0:
            inn=1
            self.linear=self.joy2[1]
            self.angular=self.joy2[0]
        if inn==1:
            if self.joy[0]==0 and self.joy[1]==0 and self.joy[2]==0 and self.joy[3]==0 and self.joy2[0]==0 and self.joy2[1]==0:
                inn=0
            else:
                pass
    def moving(self,vel_msg):
        self.velocity_publisher.publish(vel_msg)

data=Joy()
vel_msg=Twist()

''' robot position '''
turtle = robot()
turtle.callback(data) #without this, getting error
global inn, max_vel_linear, max_angular
inn=0
max_vel_linear = 3.0
max_vel_angular = 1.5 
''' main '''
if __name__ == '__main__':
 while 1:
     if inn==1:
        
        if turtle.semo==1: # Reset odometry
             #subprocess.call('',shell=True)
             p=subprocess.Popen('rostopic pub /reset std_msgs/Empty "{}"',shell=True)
             time.sleep(2)
             p.terminate()
        elif turtle.one==1: ## check that the velocity of robot always less than max_val
             for i < max_vel_linear and j < max_vel_angular:
                vel_msg.linear.x=turtle.linear*i*0.5
             
                vel_msg.angular.z=turtle.angular*z*0.3
                
                if turtle.linear==0 and turtle.angular != 0: ## check that oprater change from (X=0, Y=+1,-1) to (X=+1,-1, Y=0)
                	vel_msg.angular.z = turtle.angular*0.2
                else: 
                	 pass

                
        elif turtle.x==1: # stop robot
             vel_msg.linear.x=0
             vel_msg.angular.z=0
        turtle.moving(vel_msg)        
     else:
         print('no data in')
     turtle.rate.sleep()