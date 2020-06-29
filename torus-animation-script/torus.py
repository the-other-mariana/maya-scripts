#File:      torus.py
#Author:    Mariana Avalos
#Date:      22/03/2019
#Description: Python code that makes animation of a torus movement

import maya.cmds as cmds
import math

objs = cmds.ls(selection = True) #lista de los objetos en escena
cmds.cutKey(objs)
obj = objs[0]

r = 4
R = 8
frames = 500

if(R <= r):
    r = 2
    R = 10
if frames <= 0:
    frames = 80

xPos = 0
yPos = 0
frame = 0
freq = R * 4 # the torus will make R * 4 revolutions
for i in range(0, frames):
    frame = i
    xPos = math.cos(math.radians(360.0 / frames * i)) * (R + r*math.cos(math.radians(freq *(360.0 / frames * i))))
    zPos = math.sin(math.radians(360.0 / frames * i)) * (R + r*math.cos(math.radians(freq * (360.0 / frames * i))))
    yPos = r * math.sin(math.radians(freq * (360.0 / frames * i)))

    cmds.setKeyframe(obj + ".translateZ", value = zPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    cmds.setKeyframe(obj + ".translateX", value = xPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    cmds.setKeyframe(obj + ".translateY", value = yPos, time = frame, inTangentType = "linear", outTangentType = "linear")
    
