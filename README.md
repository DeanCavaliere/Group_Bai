# Group_Bai

Group repo for team Bai Bai Bai

# Assumptions

> The joy node is installed on RPI A

# subDrive.py

> Runs on RPI B
>
> Reads node 'joy' to grab related data
>
> It will move the tires left / right / forewards / backwards

# subDriveVM.py

> Runs on the VM
>
> Reals node 'joy' and displays corresponding data

# Commands to Run Program
> Starting ROS (in every terminal, 4 total terminal windows):

     $ source ~/catkin_ws/devel/setup.bash
     
     $ export ROS_IP=ip_address
     
     $ export ROS_MASTER_URI=ip_address:11311
     

### RPI A_Terminal1 (with joy):

     $ roscore
     
### RPI A_Terminal2 (with joy):

     $ rosparam set joy_node/dev/ "/dev/input/js0"
     
     $ rosrun joy joy_node
     
### RPI B:
     $ cd ~/catkin_ws/
     
     $ rosrun drive subDrive.py
     
### VM:

     $ rostopic echo joy

# CSV
> Running subDriveVM.py creates a csv file containing the following information:

     steering, speed


# Troubleshooting
> To test communications at any listener node run the following:

     $ rosnode ping joy_node
     
> This will let you know if the nodes can communicate which can also be done with:

     $ rostopic echo joy
     
> This displays the joy data
