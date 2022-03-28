# DIME Controller
This repository contains the installer and python wrapper for controlling an Allegro Hand attached to a Kinova JACO Arm. It is part of the official implementation of [DIME](https://arxiv.org/abs/2203.13251). The base repo containing all the information can be found at [DIME - Models](https://github.com/NYU-robot-learning/DIME-Models).

This repository contains symlinks connecting to the following repositories:

1. [Allegro Hand Controller - DIME](https://github.com/NYU-robot-learning/Allegro-Hand-Controller-DIME) 
2. [Kinova Arm Controller - DIME](https://github.com/NYU-robot-learning/Kinova-Arm-Controller-DIME)

## Setup
We would advice you to install the [Kinova SDK]( https://drive.google.com/u/0/uc?id=1UEQAow0XLcVcPCeQfHK9ERBihOCclkJ9&export=download) and then proceed with running the `setup.sh` file. The `setup.sh` installs all the required dependencies.

## Launching the controllers
You have to launch the `roslaunch` files for both the Allegro Hand and Kinova Arm separately using the following commands:
- For launching the Kinova Arm controller (this includes the gravity compensation module for the Allegro Hand):
  ```
  roslaunch kinova_arm kinova_robot.launch
  ```
- For launching the Allegro Hand controller with/without the visualizer:
  ```
  roslaunch allegro_hand allegro_hand.launch VISUALIZE:=<true|false>
  ```

## Using the python wrapper
You can import the python wrapper directly since we include this directory in `PYTHONPATH` (the `setup.sh` file takes care of this). You can run the following commands to move the robot:
```
from move_dexarm import DexArmControl

arm_controller = DexArmControl()
move_robot(allegro_angles, kinova_angles)
```

## Citation
If you use this repo in your research, please consider citing the paper as follows:
```
@article{arunachalam2022dime,
  title={Dexterous Imitation Made Easy: A Learning-Based Framework for Efficient Dexterous Manipulation},
  author={Sridhar Pandian Arunachalam and Sneha Silwal and Ben Evans and Lerrel Pinto},
  journal={arXiv preprint arXiv:2203.13251},
  year={2022}
}
```