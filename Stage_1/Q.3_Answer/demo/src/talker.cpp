#include "ros/ros.h"
#include "std_msgs/String.h"
#include <dynamic_reconfigure/server.h>
#include <demo/demo_cfgConfig.h>

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
using namespace std;
int rate;

void callback(demo::demo_cfgConfig &config, uint32_t level) {
  ROS_INFO("Reconfigure Request: %d", 
            config.rate);
  rate = config.rate;


}
int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "talker");

  
  ros::NodeHandle n;
  demo::demo_cfgConfig config;
  //int rate = config.rate;

  dynamic_reconfigure::Server<demo::demo_cfgConfig> server;
  dynamic_reconfigure::Server<demo::demo_cfgConfig>::CallbackType f;
  

  f = boost::bind(&callback, _1, _2);
  server.setCallback(f);
  
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  

 
  



  
  int count = 0;
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());
    ROS_INFO("rate = %d",rate);
    ros::Rate loop_rate(rate);

    
    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}