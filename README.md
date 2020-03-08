# Group_Bai
Group repo for team Bai Bai Bai

# Assumptions
> The joy node is running on RPI A

# pubDrive.py
> Runs on RPI A

> Reads joy node

> Posts stripped data to node 'controller'


# subDrive.py
> Runs on RPI B

> Reads node 'controller' (or we can make it read 'joy')

> It will move the tires left / right and control accel <== this needs to be merged with the existing code we did for the last HW

# pubDrive.py
> Also has the code that the VM needs to display relevent control data

# TO DO: 
> merge existing code form last HW to subDrive.py

> pandas CSV 

> camera (not necessary for this HW)
