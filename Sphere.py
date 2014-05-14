#Make a sphere using primitives and add lighting to it.
#Made By:- Vandit Sheth

import sys
import math
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Defining Slices and Stacks (Same as in glutSolidSphere)
SLICES=200;
STACKS=200;

#Flag to enable or disable lighting.
light=0

#Function to set the parameters for light
def lightfunc():
   global light
   glShadeModel(GL_SMOOTH)
   
   #Lighting Flag checked to see if lighting has to be turned enabled/disabled
   #If lighting is ON
   if light==1:
      glEnable(GL_LIGHTING)
      glEnable(GL_LIGHT0)
      glEnable(GL_DEPTH_TEST)
      glEnable(GL_COLOR_MATERIAL)

   #If lighting is OFF
   elif light==0:
      glDisable(GL_LIGHTING)
      
def display():
    global RADIUS;
    global light
    lightfunc()
    
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    position =  [10.0, 10.0, 10.0, 10.0]
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #Making thick lines to make sphere solid
    glLineWidth(10)

    #Calling the custom sphere build function, arcsphere
    glPushMatrix()
    glTranslatef(0,0,0)
    glRotatef(180,0,0,1)
    arcsphere(RADIUS,SLICES,STACKS)
    glPopMatrix()

    #Setting the Light
    glPushMatrix ()
    gluLookAt (0.0, 0.0, 4000.0, 0.0, 0.0, 0.0, 100.0, 100.0, -100.0)
    glTranslate (30.0, 30.0, 30.0)
    glLightfv (GL_LIGHT0, GL_POSITION, position)
    glPopMatrix ()

#Function that makes the sphere from arcs. Similar to glutSolidSphere()
def arcsphere(RADIUS,SLICES,STACKS):

   i=0
   #Making the longitudes of the sphere. Here arcs are made from 0-360 degrees
   while (i<=360):
      glPushMatrix();
      glRotatef(i,1,0,0)
      arc(RADIUS);
      glPopMatrix();
      i+=360/SLICES

   glRotatef(90,0,1,0);

   #Making the latitudes of the sphere. Here arcs are made from 0-360 degrees
   i=0;
   while (i<=360):
      glPushMatrix();
      glRotatef(i,1,0,0)
      arc(RADIUS);
      glPopMatrix();
      i+=360/STACKS

#Function to make one arc of the sphere by joining nearby points.
def arc(i):
    glColor3d(0.0, 0.0, 1.0)

    glBegin(GL_LINE_LOOP)

    #Make a line loop of nearby lines
    for ang in range(0, 180, 2):
        #Vertices calculated based on x=Radius*cos(angle) and y=Radius*sin(angle)
        x = i*cos(ang*pi/180)
        y = i*sin(ang*pi/180)
        glVertex2d(x, y)
    glEnd()
    glFlush()

def keyboard(key, x, y):
  global light, RADIUS

  #Enable Lighting
  if key=='l' and light==0:
     light = 1
     glutPostRedisplay();

  #Disable Lighting   
  elif key=='L' and light==1:
     light = 0
     glutPostRedisplay();

  #Increase Radius
  elif key=='r' and RADIUS<10:
     RADIUS=RADIUS+1.0
     glutPostRedisplay();
     
  #Decrease Radius     
  elif key=='R' and RADIUS>1:
     RADIUS=RADIUS-1.0
     glutPostRedisplay();
     
  #Quit
  elif key==chr(27):
     sys.exit()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutCreateWindow("Sphere")

#Taking Radius as input from the user
RADIUS=input('Enter value of radius: ')

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-10,10,-10,10,-10,10)
glutMainLoop()
