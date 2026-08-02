from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anup_x_ros2',
    maintainer_email='anup_x_ros2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main",
            "robot_news_station = my_py_pkg.robot_news_station:main",
            "smartphone = my_py_pkg.smartphone:main",
            "pub_number = my_py_pkg.pub_number:main",
            "sub_number = my_py_pkg.sub_number:main",
            "add_two_ints_server = my_py_pkg.add_two_ints_server:main",
            "add_two_ints_client_no_oop = my_py_pkg.add_two_ints_client_no_oop:main",
            "add_two_ints_client = my_py_pkg.add_two_ints_client:main",
            "project_one_pub = my_py_pkg.project_one_pub:main",
            "project_one_sub= my_py_pkg.project_one_sub:main",
            "hw_status_pub= my_py_pkg.robot_status:main",
            "led_panel = my_py_pkg.led_panel:main",
            "battery = my_py_pkg.battery:main"

        ],
    },
)
