## canny_edge_ros_opencv


**Code Explinations:**

**1. Image_converter.cpp**

+ Image converter function
~~~cpp

ImageConverter()
    : it_(nh_)
  {
    // Subscrive to input video feed and publish output video feed
    image_sub_ = it_.subscribe("/camera/rgb/image_raw", 1,
      &ImageConverter::imageCb, this);
    image_pub_ = it_.advertise("/image_converter/output_video", 1);

    cv::namedWindow(OPENCV_WINDOW);
  }

  ~ImageConverter()
  ~~~
 
  1. Subscribe the input video feed and publish  output video feed
  
  

