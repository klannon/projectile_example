#! /usr/bin/env python3

import math


if __name__ == "__main__":

    # Define some basic characteristics for the projectile

    # Starting location
    x0 = 0
    y0 = 0

    # Starting velocity
    v0 = 15
    theta0 = 45  # In degrees

    # Mass
    m = 10


    # Define some characteristics of the environment

    # Gravitational acceleration
    g = 9.81


    # Parameters for estimating the motion
    dt = 0.001

    print(f"Starting position: x0 = {x0:.2f} m, y0 = {y0:.2f} m.")
    print(f"Initial v = {v0:.2f} m/s at {theta0:.2f} degrees.")
    print(f"Projection mass m = {m:.2f}.")

    # Start the simulation with the first step

    # Find the components of the velocity for the first step
    vx = v0*math.cos(math.radians(theta0))
    vy = v0*math.sin(math.radians(theta0))

    # Set the components of the acceleration
    ax = 0
    ay = -g

    # Calculate the distance traveled in this time step, assuming
    # acceleration is constant over this small time step
    x = x0 + vx*dt + 0.5*ax*dt*dt
    y = y0 + vy*dt + 0.5*ay*dt*dt

    # Keep stepping until we reach the ground (y = 0)
    while y > 0:

        # Update the velocity components based on the acceleration
        vx += ax*dt
        vy += ay*dt

        # Update the position, assuming constant acceleration
        x += (vx*dt + 0.5*ax*dt*dt)
        y += (vy*dt + 0.5*ay*dt*dt)

    # Print out the final distance traveled
    print(f"The range is {x-x0:.2f} m")
