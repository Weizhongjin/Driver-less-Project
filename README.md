Final Project
====

## Collision warning system for self-driving vehicle.
------

### Project summary: <br>

In this project we propose to construct a collision warning system for driverless vehicle to detect dynamic objects in the drivable region. Through the input video from driving recorder, the system can estimate the drivable space in 3D, provide category of obstacles present in lane, and eventually output “Go” and “Stop” command. To implement these function, we need to train convolutional neural networks for object detection and semantic segmentation. <br>

### Detail:<br>

#### * Database: <br>
[Berkeley self-drive database](https://deepdrive.berkeley.edu/)   and [KITTI Database](http://www.cvlibs.net/datasets/kitti/) <br>
#### * Pyhton code base: <br>
[Keras or Caffe or Pytoch](https://github.com/pytorch/pytorch) <br>
#### * Deep learning Network:<br>
[Faster-R-CNN](https://github.com/Weizhongjin/faster-rcnn.pytorch)<br>
Yolo[paper](https://arxiv.org/abs/1506.02640),[Detail in Yolo](https://blog.csdn.net/u014380165/article/details/72616238),[PPT](https://docs.google.com/presentation/d/1aeRvtKG21KHdD5lg6Hgyhx5rPq_ZOsGjG5rJ1HP7BbA/pub?start=false&loop=false&delayms=3000&slide=id.g137784ab86_4_4107),[code](https://github.com/pjreddie/darknet)<br>
#### * Focus on :<br>
Novality of the network, usc bagnet to substitute the traditional cnn. <br>

### Reference:  <br>

#### * Paper<br>
1.	Ross Girshick. “Fast R-CNN”, IEEE International Conference on Computer Vision. 2015.<br>
2.	[S. Ren, K. He, R. Girshick and J. Sun. “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks”, 2017 IEEE Transactions on Pattern Analysis and Machine Intelligence](https://arxiv.org/pdf/1506.01497.pdf) <br>
3.  Wieland Brendel, Matthias Bethge. “Approximating CNNs with Bag-of-local-Features models works surprisingly well on ImageNet”, ICLR 2019 Conference Blind Submission <br>

4.  [R. Zhang, Y. Yang, W. Wang, L. Zeng, J. Chen and S. McGrath, "An Algorithm for Obstacle Detection based on YOLO and Light Filed Camera," 2018 12th International Conference on Sensing Technology (ICST), Limerick, 2018, pp. 223-226.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8603600&isnumber=8603546)<br>

5. [J. Lin and M. Sun, "A YOLO-Based Traffic Counting System," 2018 Conference on Technologies and Applications of Artificial Intelligence (TAAI), Taichung, 2018, pp. 82-85.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8588483&isnumber=8588436)<br>

6. [H. Jeong, K. Park and Y. Ha, "Image Preprocessing for Efficient Training of YOLO Deep Learning Networks," 2018 IEEE International Conference on Big Data and Smart Computing (BigComp), Shanghai, 2018, pp. 635-637.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8367193&isnumber=8367080)<br>

7.  [Z. Xu, H. Shi, N. Li, C. Xiang and H. Zhou, "Vehicle Detection Under UAV Based on Optimal Dense YOLO Method," 2018 5th International Conference on Systems and Informatics (ICSAI), Nanjing, 2018, pp. 407-411.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8599403&isnumber=8599286)<br>

8.  [T. Santad, P. Silapasupphakornwong, W. Choensawat and K. Sookhanaphibarn, "Application of YOLO Deep Learning Model for Real Time Abandoned Baggage Detection," 2018 IEEE 7th Global Conference on Consumer Electronics (GCCE), Nara, 2018, pp. 157-158.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8574819&isnumber=8574475)<br>

9.  [A. Ćorović, V. Ilić, S. Durić, M. Marijan and B. Pavković, "The Real-Time Detection of Traffic Participants Using YOLO Algorithm," 2018 26th Telecommunications Forum (TELFOR), Belgrade, 2018, pp. 1-4.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8611986&isnumber=8611788>)<br>

10. [L. Sommer, N. Schmidt, A. Schumann and J. Beyerer, "Search Area Reduction Fast-RCNN for Fast Vehicle Detection in Large Aerial Imagery," 2018 25th IEEE International Conference on Image Processing (ICIP), Athens, 2018, pp. 3054-3058.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8451189&isnumber=8451009)<br>

11. [G. Chandan, A. Jain, H. Jain and Mohana, "Real Time Object Detection and Tracking Using Deep Learning and OpenCV," 2018 International Conference on Inventive Research in Computing Applications (ICIRCA), Coimbatore, 2018, pp. 1305-1308.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8597266&isnumber=8596764)<br>

12. [L. A. Marina, F. D. Moldoveanu and S. M. Grigorescu, "Environment perception in racing simulators using Deep Neural Networks," 2017 International Conference on Optimization of Electrical and Electronic Equipment (OPTIM) & 2017 Intl Aegean Conference on Electrical Machines and Power Electronics (ACEMP), Brasov, 2017, pp. 1102-1107.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=7975119&isnumber=7974934)<br>

13. [W. Liu, S. Liao, W. Hu, X. Liang and Y. Zhang, "Improving Tiny Vehicle Detection in Complex Scenes," 2018 IEEE International Conference on Multimedia and Expo (ICME), San Diego, CA, 2018, pp. 1-6.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8486507&isnumber=8486434)<br>

14. [M. Sheng, C. Liu, Q. Zhang, L. Lou and Y. Zheng, "Vehicle Detection and Classification Using Convolutional Neural Networks," 2018 IEEE 7th Data Driven Control and Learning Systems Conference (DDCLS), Enshi, 2018, pp. 581-587.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8516099&isnumber=8515899)<br>

15. [C. Guindel, D. Martin and J. M. Armingol, "Fast Joint Object Detection and Viewpoint Estimation for Traffic Scene Understanding," in IEEE Intelligent Transportation Systems Magazine, vol. 10, no. 4, pp. 74-86, winter 2018.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8464061&isnumber=8501998)<br>

16. [S. Wu and Y. Xu, "DSN: A New Deformable Subnetwork for Object Detection," in IEEE Transactions on Circuits and Systems for Video Technology.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8667874&isnumber=4358651)<br>

17. [M. Manana, C. Tu and P. A. Owolawi, "Preprocessed Faster RCNN for Vehicle Detection," 2018 International Conference on Intelligent and Innovative Computing Applications (ICONIC), Plaine Magnien, 2018, pp. 1-4.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8601243&isnumber=8601084)<br>

18. [M. Roh and J. Lee, "Refining faster-RCNN for accurate object detection," 2017 Fifteenth IAPR International Conference on Machine Vision Applications (MVA), Nagoya, 2017, pp. 514-517.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=7986913&isnumber=7986754)<br>

19. [W. Wang, B. Wu, S. Yang and Z. Wang, "Road Damage Detection and Classification with Faster R-CNN," 2018 IEEE International Conference on Big Data (Big Data), Seattle, WA, USA, 2018, pp. 5220-5223.](http://ieeexplore.ieee.org.libproxy1.usc.edu/stamp/stamp.jsp?tp=&arnumber=8622354&isnumber=8621858)


#### * Useful Website: <br>
[Coursera courses:visual-perception-self-driving-cars](https://www.coursera.org/learn/visual-perception-self-driving-cars) <br>
[KITTI数据集简介与使用](https://blog.csdn.net/Solomon1558/article/details/70173223)<br>
[KITTI数据使用序列——3D Object检测数据集使用](https://blog.csdn.net/hit1524468/article/details/79766805)<br>

### Machine: <br>

Mac osx: Program <br>
AWS p3.2xlarge GPU: Training Network<br>
Final Data: [VOC Form KITTI](https://s3.amazonaws.com/weizhongjin/VOC2012.zip)<br>

