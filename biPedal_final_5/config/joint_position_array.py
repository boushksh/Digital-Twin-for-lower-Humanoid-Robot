#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rospy.rostime import Duration


def control_robot():
    rospy.init_node('robot_controller', anonymous=True)
    pub_left_leg = rospy.Publisher('/left_leg_controller/command', JointTrajectory, queue_size=10)
    pub_right_leg = rospy.Publisher('/right_leg_controller/command', JointTrajectory, queue_size=10)

    rospy.sleep(1)  # Wait for publishers to initialize
    rate = rospy.Rate(10)  # 10Hz control rate
    x = input("\nPress any key to start ")

    # Predefined joint positions for both legs
    predefined_left_positions = [
        [0.0, -0.7, 0.7, 0.0],
        [0, 0, 0, 0],
        [0, 0.7, -0.7, 0],
        [0, 0, 0, 0],
        [0.0, -0.7, 0.7, 0.0],
        [0, 0, 0, 0],
        [0, 0.7, -0.7, 0],
        [0, 0, 0, 0]
    ]

    predefined_right_positions = [
        [0, 0, 0, 0],
        [0.0, 0.7, 0.7, 0.0],
        [0, 0, 0, 0],
        [0, -0.7, -0.7, 0],
        [0, 0, 0, 0],
        [0.0, 0.7, 0.7, 0.0],
        [0, 0, 0, 0],
        [0, -0.7, -0.7, 0]
    ]

    while not rospy.is_shutdown():
    # Loop through predefined positions and publish trajectories
        for left_positions, right_positions in zip(predefined_left_positions, predefined_right_positions):
            # Construct joint trajectory message for the left leg
            left_traj = JointTrajectory()
            left_traj.joint_names = ["j_left_hip", "j_left_upper_leg", "j_left_lower_leg", "j_left_foot"]
            left_point = JointTrajectoryPoint()
            left_point.positions = left_positions
            left_point.time_from_start = Duration(0, 100000000)  # Set duration to 10 seconds (adjust as needed)
            left_traj.points.append(left_point)

            # Construct joint trajectory message for the right leg
            right_traj = JointTrajectory()
            right_traj.joint_names = ["j_right_hip", "j_right_upper_leg", "j_right_lower_leg", "j_right_foot"]
            right_point = JointTrajectoryPoint()
            right_point.positions = right_positions
            right_point.time_from_start = Duration(0, 100000000)  # Set duration to 10 seconds (adjust as needed)
            right_traj.points.append(right_point)

            # Publish trajectories for both legs
            pub_left_leg.publish(left_traj)
            rospy.sleep(0.1)
            pub_right_leg.publish(right_traj)

            rate.sleep()
            print("Done \n")
           # x = input("\nPress any key to start ")


if __name__ == '__main__':
    try:
        control_robot()
    except rospy.ROSInterruptException:
        pass










   # predefined_left_positions = [
   #      [0.0, -0.7, 0.7, 0.0],
   #      [0, 0, 0, 0],
   #      [0, 0.7, -0.7, 0],
   #      [0, 0, 0, 0],
   #      [0.0, -0.7, 0.7, 0.0],
   #      [0, 0, 0, 0],
   #      [0, 0.7, -0.7, 0],
   #      [0, 0, 0, 0]
   #  ]
   #
   #  predefined_right_positions = [
   #      [0, 0, 0, 0],
   #      [0.0, 0.7, 0.7, 0.0],
   #      [0, 0, 0, 0],
   #      [0, -0.7, -0.7, 0],
   #      [0, 0, 0, 0],
   #      [0.0, 0.7, 0.7, 0.0],
   #      [0, 0, 0, 0],
   #      [0, -0.7, -0.7, 0]
   #  ]




    # predefined_left_positions = [
    #     [0.0, -0.288, 0.337, 0.2492],
    #     [0.0, -0.288, 0.337, 0.2492],
    #     [0, -0.123, 0.3754, 0.2492],
    #     [0, -0.123, 0.3754, 0.2492]
    # ]
    #
    # predefined_right_positions = [
    #     [0, 0.0902, 0.2377, -0.188],
    #     [0.0, 0.24, 0.304, -0.117],
    #     [0.0, 0.24, 0.304, -0.117],
    #     [0, 0.0902, 0.2377, -0.188]
    # ]



