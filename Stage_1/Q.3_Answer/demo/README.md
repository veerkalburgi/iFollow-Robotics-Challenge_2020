## ROS Publisher and Subscriber with dynamic reconfigure

**Yes, C++ is Faster than Python. C++ source code needs to become a machine code, whereas the python need interpreter which makes python slow.**

**A.** In a combination where c++ publisher and python subscriber, the actual rate is 90 Hz, and measured rate is 84.48.
       
   In a combination where C++ publisher and c++ subscriber, the actual rate is 90 Hz and measured rate is 84.48
       
   In a combination where python publisher and python subscriber, the actual rate is 20 and measured rate is 17.
       
   In a combination where python publisher and c++ subscriber, the actual rate is 30 and measured rate is 26.57
       
       
**B.** From this perfromance difference I understod that, first thing c++ is better for the higher frequence, for the lower frequnce we can use the python publisher and      subscriber.
      
   Second thing is that combination is really matter when we want to get desired rate. 
      
**C.** While dealing with roscpp we should have to make that cpp file excutable we have to add excutable, dependencies and target_linke_library. Here we are working with configure file to change the publishing rate using dynamic reconfigure GUI, so we have to add the .cfg file in Cmake.txt and dependacecies. Where as when we are working with rospy didn't need to worry about those all things we did for roscpp, using import libraires we can use dynamic reconfigure. 

As we did different experiment above(a,b,c,d) we understood the how these effect the result.
