# Projectile Motion Example Program
## Overview
This repository provides a basic Python program for calculating projectile motion.  This is meant to give physics students a familar problem they can play with while learning python.  You can run the program as follows:
```
python3 projectile.py
```

If it runs properly, it should output the following to your terminal screen:
```
Starting position: x0 = 0.00 m, y0 = 0.00 m.
Initial v = 15.00 m/s at 45.00 degrees.
Projection mass m = 10.00.
The range is 22.94 m
```

You can get a sense for how the program works by editing the source file `projectile.py` to make small changes (e.g. change the angle, initial speed, etc.).  This will help you get a basic sense for how this code works.  To go beyond, this basic understanding, consider some of the suggestions below.

## Next Steps
In order to push your mastery of Python (and refresh your knowledge of physics), try to make the following modifications to this program:

### Basic Python Programming Skills
* Change some of the initial values and/or parameters and see what changes
* Calculate the angle of the velocity vector at the point where it hits the ground
* Add in drag force
* Give the projectile an electric charge and place another charge somewhere along the xaxis
* Put the range calculation inside a function and run the calculation by calling the function
* Make the program read in the initial values and the starting configuration from a file
* Have the program write out the x and y coordinates from each time step to a file
* Have the program take some or all of its configuration information from the command line
* Using the range function that you wrote above, have the program determine the initial angle required to hit a particular range. Do this by guessing angles and seeing whether the calculated range is too long or too short. Continue refining your guess until it is close enough (within some defined tolerance in your program) to the requested range.

### Scientific Python (numpy, pandas, matplotlib)
* Make y vs x, x vs t, y vs t, vx vs t, vy vs t plots from the projectile's trajectory.  If you add a magnetic field, you'll want to plot all of the x, y, z points of the projectile's motion (matplotlib)
* Store the trajectory in a pandas data frame and use that to make the above plots (pandas)
