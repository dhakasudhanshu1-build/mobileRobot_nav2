from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    robot_description = PathJoinSubstitution([
        FindPackageShare('nav2_mobile_robot'),
        'nav2_mobile_robot.xacro'
    ])

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', robot_description])
            }]
        )
        # No RViz, no GUI - clean TF only
    ])
