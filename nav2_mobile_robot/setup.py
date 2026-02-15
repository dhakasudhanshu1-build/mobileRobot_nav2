from setuptools import find_packages, setup

package_name = 'nav2_mobile_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['urdf/nav2_mobile_robot.xacro']),
        ('share/' + package_name, ['urdf/nav2_mobile_robot_macro.xacro']),
        ('share/' + package_name, ['launch/display.launch.py']),
        ('share/' + package_name, ['worlds/maze.sdf']),
        ('share/' + package_name, ['launch/nav2_mobile_robot_gazebo.launch.py']),
        ('share/' + package_name, ['launch/slam.launch.py']),
        ('share/' + package_name, ['conf/slam.yaml']),
        ('share/' + package_name, ['launch/map_server.launch.py']),
        ('share/' + package_name, ['map/map.yaml']),
        ('share/' + package_name, ['map/map.pgm']),
        ('share/' + package_name, ['conf/amcl.yaml']),
        ('share/' + package_name, ['launch/amcl.launch.py']),
        ('share/' + package_name, ['launch/robot_state.launch.py']),


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sudhanshu',
    maintainer_email='dhakasudhanshu1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
