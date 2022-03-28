import rospy

from allegro_hand.controller import AllegroController
from kinova_arm.controller import KinovaController

KINOVA_HOME_VALUES = [0.07954489, 3.682943  , 0.8321387 , 3.46947199, 1.68616034, 4.02400764, 0.]

# KINOVA_SPIN_HOME_VALUES = [5.5437746094856255, 4.2607474858597865, 0.664856368504546, 3.5294253410286154, 2.197921095554227, 1.2341735639572078]
KINOVA_SPIN_HOME_VALUES = [5.383091719851259, 4.207704241164242, 0.652398833294455, 3.553339462353091, 2.099099176984657, 1.2785677935385562]
# KINOVA_SPIN_POS_VALUES = [5.546553884399233, 4.431675556207688, 0.7259855029017888, 3.5115158490139415, 2.256377082007303, 1.289027491877897]

ALLEGRO_HOME_VALUES = [ 0.        , -0.17453293,  0.78539816,  0.78539816,  0.        ,
    -0.17453293,  0.78539816,  0.78539816,  0.08726646, -0.08726646,
    0.87266463,  0.78539816,  1.04719755,  0.43633231,  0.26179939,
    0.78539816]

class DexArmControl():
    def __init__(self):
        try:
            rospy.init_node("dex_arm")
        except:
            pass
    
        self.allegro = AllegroController()
        self.kinova = KinovaController()

    def home_robot(self):
        # Homing the Kinova Arm
        self.kinova.joint_movement(KINOVA_HOME_VALUES, False)

        # Homing the Allegro Hand
        self.allegro.hand_pose(ALLEGRO_HOME_VALUES)

    def spin_pos_arm(self):
        # Homing the Allegro Hand
        self.allegro.hand_pose(ALLEGRO_HOME_VALUES)

        # Homing the Kinova Arm
        self.kinova.joint_movement(KINOVA_SPIN_HOME_VALUES, False)

        # rospy.sleep(5)
        # self.kinova.joint_movement(KINOVA_SPIN_POS_VALUES, False)

    def move_robot(self, allegro_angles, kinova_angles):
        self.kinova.joint_movement(kinova_angles, False)
        self.allegro.hand_pose(allegro_angles)

    def move_hand(self, allegro_angles):
        self.allegro.hand_pose(allegro_angles)

    def move_arm(self, kinova_angles):
        self.kinova.joint_movement(kinova_angles, False)

if __name__ == '__main__':
    dex_arm = DexArmControl()
    dex_arm.home_robot()
