#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rospy.rostime import Duration

def control_robot():
    rospy.init_node('robot_controller', anonymous=True)
    pub_left_leg = rospy.Publisher('/left_leg_controller/command', JointTrajectory, queue_size=10)
    pub_right_leg = rospy.Publisher('/right_leg_controller/command', JointTrajectory, queue_size=10)

    rospy.sleep(2)  # Wait for publishers to initialize
    rate = rospy.Rate(10)  # 10Hz control rate
    x=input("\nPress any key to start")
    
    while not rospy.is_shutdown():
    
        left_positions = [float(x) for x in input("Enter desired joint positions for left leg (comma-separated): ").split(",")]
        right_positions = [float(x) for x in input("Enter desired joint positions for right leg (comma-separated): ").split(",")]
        # Construct joint trajectory message
        left_traj = JointTrajectory()
        left_traj.joint_names = ["j_left_hip", "j_left_upper_leg", "j_left_lower_leg", "j_left_foot"]
        left_point = JointTrajectoryPoint()
        # Populate joint positions, velocities, accelerations if needed
        left_point.positions = left_positions
        left_point.time_from_start = Duration(0, 100000000)  # Set duration to 10 seconds (adjust as needed)
        left_traj.points.append(left_point)

        right_traj = JointTrajectory()
        right_traj.joint_names = ["j_right_hip", "j_right_upper_leg", "j_right_lower_leg", "j_right_foot"]
        right_point = JointTrajectoryPoint()
        # Populate joint positions, velocities, accelerations if needed
        right_point.positions = right_positions
        right_point.time_from_start = Duration(0, 100000000)  # Set duration to 10 seconds (adjust as needed)
        right_traj.points.append(right_point)

        # Publish trajectories
        pub_left_leg.publish(left_traj)
        pub_right_leg.publish(right_traj)

        rate.sleep()
        print("Done \n")
if __name__ == '__main__':
    try:
        control_robot()
    except rospy.ROSInterruptException:
        pass









