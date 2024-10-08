#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
import trajectory_msgs.msg
import matplotlib.pyplot as plt

class JointPositionPlotter:
    def __init__(self):
        rospy.init_node('joint_position_plotter', anonymous=True)
        self.joint_positions = {joint_name: [] for joint_name in ["j_left_hip", "j_left_upper_leg", "j_left_lower_leg", "j_left_foot"]}
        self.input_commands = {joint_name: [] for joint_name in ["j_left_hip", "j_left_upper_leg", "j_left_lower_leg", "j_left_foot"]}
        self.rate = rospy.Rate(1)  # Adjust the rate as needed
        rospy.Subscriber('/joint_states', JointState, self.joint_state_callback)
        rospy.Subscriber('/left_leg_controller/command', trajectory_msgs.msg.JointTrajectory, self.command_callback)

    def joint_state_callback(self, msg):
        for joint_name, position in zip(msg.name, msg.position):
            if joint_name in self.joint_positions:
                self.joint_positions[joint_name].append(position)

    def command_callback(self, msg):
        for point in msg.points:
            for i, joint_name in enumerate(msg.joint_names):
                if joint_name in self.input_commands:
                    self.input_commands[joint_name].append(point.positions[i])

    def plot_joint_data(self, joint_name):
        plt.figure(figsize=(10, 5))
        plt.plot(self.joint_positions[joint_name], label=f'{joint_name} Position')
        plt.plot(self.input_commands[joint_name], '--', label=f'{joint_name} Command', color='orange')
        plt.xlabel('Time')
        plt.ylabel('Position / Command')
        plt.title(f'Joint {joint_name} Position and Input Command over Time')
        plt.legend()
        plt.show()

    def plot_all_joints_data(self):
        for joint_name in self.joint_positions.keys():
            self.plot_joint_data(joint_name)
            self.rate.sleep()  # Sleep to control the rate

if __name__ == '__main__':
    plotter = JointPositionPlotter()
    plotter.plot_all_joints_data()
    rospy.spin()  # Keep the node running
