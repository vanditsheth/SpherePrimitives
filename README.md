SpherePrimitives
================

Makes a sphere using primitives (lines) and adds lighting

The code generates a sphere from arcs which in turn are generated from lines joining close points on the arc. First, a longitudinal cage of circles is created, then after translating by 90 degrees the latitudes are created. The number of longitudes correspond to the number of slices while the number of latitudes correspond to the number of stacks. The stacks and slices have been kept 200 each and can be changed but lower than 200 is not recommended for smoothness. Radius of the sphere is taken as input from the user when the program starts. An arcsphere function, which is an alternative to glutSolidSphere has been made, which takes Radius, Slices and Stacks as parameters and displays a sphere. This is similar to the functionality of glutSolidSphere(). The arcsphere in turn calls the arc function which makes arc based on x=radius*cos(angle), y=radius*sin(angle). Hence, the sphere is made, arc-by-arc. Also, the option of turning the light ON or OFF is given to the user and s/he can do it on key presses. Even though radius is taken as input from the user, it can be changed while the program is running. Making a sphere is computationally heavy; nence, redisplay calls are kept inside the conditional loops and keys except those in controls are plainly ignored.

The modules used here are: arcsphere, which is the calling function to make the arcs which make sphere. It is similar to glutSolidSphere(). Other module here is arc, which makes an arc, when it is called from arcsphere. These arcs combine to make sphere. Other module is the keyboard key handling module which decides actions based on key presses.

USER INPUTS:- Radius of the sphere; asked at the start.

CONTROLS
KEY		ACTION
l		Turn Lighting ON
L		Turn Lighting OFF

r		Increase radius of sphere (Maximum radius is 10)
R		Decrease radius of sphere (Minimum radius is 1)

Esc		Exit the program

NOTE:- Here the input is taken in console window and the sphere is displayed in a new display window. The window focus doesn't change automatically and the display window will have to be clicked once.
