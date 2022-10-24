# Probabilistic Robotics Algorithms

This repository contains my implementations of key algorithms from the [Probabilistic Robotics](http://robots.stanford.edu/probabilistic-robotics/) book by Thrun et al.

The repository implements the algorithms by using the turtlebot-3 simulation environment for the generating the IMU and Odometry messages.    

Key algorithms to be implemented:

- [ ] Recursive Bayes Filter
- [ ] Kalman Filter
- [ ] Partice Filter  


## SETUP
---
```
Requirements : Ubuntu 20.04  
ROS : Noetic
```

## Installing the Repository
```
$ cd ~catkin_ws/src
$ git clone https://github.com/8ajpai/probabilistic-robotics-algorithms.git
$ cd ..
$ vcs import src < src/probabilistic-robotics-algorithms/dependencies.repos
$ catkin build
$ source devel/setup.bash
```

## Running the Code
```
Run Turtlebot 
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch

Run the Tele-Operation Node 
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py

The odom-to-trajectory package coverts /odom messages to a trajectory.
$ roslaunch odom_to_trajectory create_trajectory.launch
```

Now, you can run the filtering packages.