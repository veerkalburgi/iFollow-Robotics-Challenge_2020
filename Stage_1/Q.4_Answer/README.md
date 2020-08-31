## canny_edge_ros_opencv


**Code Explinations:**

**1. Image_converter.cpp**

+ Image converter function
~~~cpp

ImageConverter()
    : it_(nh_)
  {
    
    image_sub_ = it_.subscribe("/camera/rgb/image_raw", 1,
      &ImageConverter::imageCb, this);
    image_pub_ = it_.advertise("/image_converter/output_video", 1);

    cv::namedWindow(OPENCV_WINDOW);
  }

  ~ImageConverter()
  ~~~
 
  1. Subscribe the input video feed and publish  output video feed
  
  + cvbridge 
 
 ~~~cpp
   
   void imageCb(const sensor_msgs::ImageConstPtr& msg)
  {
    cv_bridge::CvImagePtr cv_ptr;
    try
    {
      cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }
 ~~~
 
 2. Helps to coversion between ROS Images to opencv images**
  
  

