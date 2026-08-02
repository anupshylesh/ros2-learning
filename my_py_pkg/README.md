# ROS 2 ython Package



A collection of ROS 2 Python exercises and robotics communication examples developed using **ROS 2 Jazzy**, **Ubuntu Linux**, and **Python**.



## Topics Covered



- ROS 2 Services and Clients

- Inter-node Communication

- Robot Status Publishing

- Battery Status

- LED Control

- Object-Oriented Programming

- Basic Robotics Communication



## Python Examples



| File | Description |

|---|---|

| `add_two_ints_server.py` | ROS 2 service server |

| `add_two_ints_client.py` | ROS 2 service client |

| `robot_news_station.py` | Publishes robot news |

| `battery.py` | Battery status example |

| `led_panel.py` | LED panel control example |

| `smartphone.py` | ROS 2 communication and Python OOP example |



## Environment



- **ROS 2:** Jazzy

- **OS:** Ubuntu Linux

- **Language:** Python 3

- **ROS 2 Python Library:** `rclpy`



## Package Structure



```text

my_py_pkg/

├── package.xml

├── setup.py

├── setup.cfg

├── resource/

├── my_py_pkg/

│   ├── add_two_ints_server.py

│   ├── add_two_ints_client.py

│   ├── robot_news_station.py

│   ├── robot_status.py

│   ├── battery.py

│   ├── led_panel.py

│   └── smartphone.py

└── test/
