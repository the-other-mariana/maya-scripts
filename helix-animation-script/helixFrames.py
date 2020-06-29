#File:      helixFrames.py
#Author:    Mariana Avalos
#Date:      21/03/2019
#Description: Python code that makes animation of a helix movement

import maya.cmds as cmds
import math

objs = cmds.ls(selection = True) #lista de los objetos en escena
cmds.cutKey(objs)
obj = objs[0]


radius = 5
revs = 4
totalFrames = 100
height = 20

if radius <= 0:
    radius = 5
if revs <= 0:
    revs = 3
if totalFrames <= 0:
    totalFrames = 75
if height <= 0:
    height = 20

xPos = 0
yPos = 0
frame = 0
frames = int(totalFrames / (revs * 1.00))
dy = height / (frames *revs * 1.0)

for i in range(0, frames *(revs) ):
    frame = i
    xPos = math.cos(math.radians(360.0 / frames * i)) * radius
    zPos = math.sin(math.radians(360.0 / frames * i)) * radius
    yPos += dy

    cmds.setKeyframe(obj + ".translateZ", value = zPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    cmds.setKeyframe(obj + ".translateX", value = xPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    cmds.setKeyframe(obj + ".translateY", value = yPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    
