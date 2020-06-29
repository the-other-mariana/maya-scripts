#File:      coolCylinder.py
#Author:    Mariana Avalos
#Date:      04/03/2019
#Description: Python code that makes a 3D cylinder

import maya.cmds as c
import math
import maya.OpenMaya as OM

sides = 12
radius = 5
segments = 11
height = 13

verts = []
mesh = OM.MFnMesh()
mergeVerts = True
pointTolerance = 0.001

temp = OM.MPoint(0, 0, 0)
verts.append(temp)

for j in range(segments + 1):
    posY = (height*1.00 / (segments)) * j
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
