#File:      circleFrames.py
#Author:    Mariana Avalos
#Date:      21/03/2019
#Description: Python code that makes animation of a circle movement

import maya.cmds as cmds
import math

objs = cmds.ls(selection = True) #lista de los objetos en escena
cmds.cutKey(objs)
obj = objs[0]

xPos = 0
yPos = 0
frame = 0
radius = 5
frames = 100

if radius <= 0:
    radius = 4
if frames <= 0:
    frames = 50


for i in range(0, frames):
    frame = i
    xPos = math.cos(math.radians(360.0 / frames * i)) * radius
    zPos = math.sin(math.radians(360.0 / frames * i)) * radius

    cmds.setKeyframe(obj + ".translateZ", value = zPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    cmds.setKeyframe(obj + ".translateX", value = xPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    
