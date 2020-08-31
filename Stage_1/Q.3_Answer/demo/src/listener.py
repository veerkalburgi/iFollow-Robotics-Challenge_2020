#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#import dynamic_reconfigure.client

def callback(data):
    #rospy.loginfo("Config set to {rate}".format(**config))
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    #client = dynamic_reconfigure.client.Client("demo", timeout=30, config_callback=callback)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
