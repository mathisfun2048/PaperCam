If you're here, you're probably wondering what each of these files does. 

1. camera_main.py: This is the runtime firmware. It ensures that the functionality we want is achieved. This includes coordinating taking pictures, displaying pictures, storing pictures, timestamps, shutter animation, debouse logic, and low battery indicator (among other things). 
2. papercam.service: This is the ststemd unit. This is what launches the firmware and resets the python script if it crashes. It also logs these crashes. 
3. install_papercam.sh: This is the bootstrapper. It verifies the root, installs OS packages, runs python packages, enables pi interfaces, creates runtime directories (for instance a photos folder), moves the firmware to its appropriate place, creates a systemd unit (the above file!), auto-boots teh firmware, and creates logs. This is what allows the above 2 to do their jobs!
   
