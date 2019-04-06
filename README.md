#Final Project 
====
##Collision warning system for self-driving vehicle.
-------
###Project summary: 
-----
In this project we propose to construct a collision warning system for driverless vehicle to detect dynamic objects in the drivable region. Through the input video from driving recorder, the system can estimate the drivable space in 3D, provide category of obstacles present in lane, and eventually output “Go” and “Stop” command. To implement these function, we need to train convolutional neural networks for object detection and semantic segmentation.
###Detail:
-----
####Database: 
Berkeley self-drive database( https://deepdrive.berkeley.edu/   KITTI Database( http://www.cvlibs.net/datasets/kitti/ )
####Pyhton code base: 
Keras or Caffe or Pytoch
####Deep learning Network:
Faster-R-CNN, Yolo
####Focus on :
Novality of the network, usc bagnet to substitute the traditional cnn.

###Reference:  
-----
####Paper
1.	Ross Girshick. “Fast R-CNN”, IEEE International Conference on Computer Vision. 2015.
2.	S. Ren, K. He, R. Girshick and J. Sun. “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks”, 2017 IEEE Transactions on Pattern Analysis and Machine Intelligence.
3.  Wieland Brendel, Matthias Bethge. “Approximating CNNs with Bag-of-local-Features models works surprisingly well on ImageNet”, ICLR 2019 Conference Blind Submission

####Useful Website: 
Coursera courses: https://www.coursera.org/learn/visual-perception-self-driving-cars 

###Machine: 
-----
Mac osx: Program 
AWS p3.2xlarge GPU: Training Network