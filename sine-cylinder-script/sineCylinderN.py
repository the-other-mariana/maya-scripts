#File:      sineCylinderN.py
#Author:    Mariana Avalos
#Date:      18/03/2019
#Description: Python code that makes a 3D cylinder with sine wave spikes.

import maya.cmds as c
import math
import maya.OpenMaya as OM

n = 5
sides = 12
radius1 = 5
radius2 = 6
segments = 41
height = 37

verts = []
mesh = OM.MFnMesh()
mergeVerts = True
pointTolerance = 0.001
temp = OM.MPoint(0, 0, 0)
verts.append(temp)
Pi = 3.1416

radius2 = radius2 / 2.0

for j in range(segments + 1):
    radius = 0
    posY = (height*1.00 / (segments)) * j
    radius = (radius2) * math.sin(posY*(n*1.0 / (height / (2*Pi) ) ) - 0.5*Pi) + radius1 + (radius2)
    for i in range(sides):
        posX = math.cos(math.radians(360.0/sides * i)) * radius
        posZ = math.sin(math.radians(360.0/sides * i)) * radius
        temp = OM.MPoint(posX, posY, posZ)
        verts.append(temp)

temp = OM.MPoint(0, height, 0)
verts.append(temp)

baseArray = OM.MPointArray()
baseArray.setLength(3)
for j in range(2):
    exception = 0
    for i in range(sides):
        if(i == sides - 1):
            exception = sides
        baseArray.set(verts[0 + j * (len(verts) - 1)], 0)
        baseArray.set(verts[(i + 1) + j * (sides * segments)], 1)
        baseArray.set(verts[(i + 2 - exception) + j * (sides * segments)], 2)
        mesh.addPolygon(baseArray, mergeVerts, pointTolerance)

quadArray = OM.MPointArray()
quadArray.setLength(4)
for j in range(0, segments):
    exception = 0
    for i in range(sides):
        if(i == sides -1):
            exception = sides
        quadArray.set(verts[(i + 1) + (sides * j)], 0)
        quadArray.set(verts[(i + 2 - exception) + (sides * j)], 1)
        quadArray.set(verts[(i + (sides + 2) - exception) + (sides * j)], 2)
        quadArray.set(verts[(i + (sides + 1)) + (sides * j)], 3)
        mesh.addPolygon(quadArray, mergeVerts, pointTolerance)
