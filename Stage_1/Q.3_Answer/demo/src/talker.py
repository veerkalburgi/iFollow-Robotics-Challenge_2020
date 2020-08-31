#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from dynamic_reconfigure.server import Server as DynamicReconfigureServer
from demo.cfg import demo_cfgConfig as ConfigType


class NodeExample(object):
    def __init__(self):
        

        self.server = DynamicReconfigureServer(ConfigType, self.reconfigure)
        
        # Create a publisher for our custom message.
        pub = rospy.Publisher('chatter', String, queue_size=10)
        

    
        
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            rospy.loginfo('rate = %d',self.rate)
            rate =self.rate
            pub.publish(hello_str)
            r =rospy.Rate(rate)
            r.sleep()
    def reconfigure(self, config, level):
        # Fill in local variables with values received from dynamic reconfigure clients (typically the GUI).
        self.rate = config["rate"]
        # Return the new variables.
        return config


#Main Functio
if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    try:
        ne = NodeExample()
    except rospy.ROSInterruptException:
        pass
