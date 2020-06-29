#File:      house.py
#Author:    Mariana Avalos
#Date:      27/02/2019
#Description: Python code that makes a 3D house
import maya.OpenMaya as OM

mesh = OM.MFnMesh()
mergeVerts = True
pointTolerance = 0.001
verts = [
        OM.MPoint(-2, 0, 2),
        OM.MPoint(2, 0, 2),
        OM.MPoint(2, 0, -2),
        OM.MPoint(-2, 0, -2),

        OM.MPoint(-2, 4, 2),
        OM.MPoint(2, 4, 2),
        OM.MPoint(2, 4, -2),
        OM.MPoint(-2, 4, -2),

        OM.MPoint(0, 6, 0)
        ]

sqrVertexArray = OM.MPointArray()
sqrVertexArray.setLength(4)
for i in range(0, 4):
    sqrVertexArray.set(verts[i], i)
mesh.addPolygon(sqrVertexArray, mergeVerts, pointTolerance)

exception = 0
for i in range(0, 4):
    sqrVertexArray = OM.MPointArray()
    sqrVertexArray.setLength(4)
    if i == 3:
       exception = 4
    sqrVertexArray.set(verts[i], 0)
    sqrVertexArray.set(verts[i + 1 - exception], 1)
    sqrVertexArray.set(verts[i + 5 - exception], 2)
    sqrVertexArray.set(verts[i + 4], 3)
    mesh.addPolygon(sqrVertexArray, mergeVerts, pointTolerance)

exception = 0
for i in range(4, 8):
    sqrVertexArray = OM.MPointArray()
    sqrVertexArray.setLength(3)
    if i == 7:
        exception = 4
    sqrVertexArray.set(verts[i], 0)
    sqrVertexArray.set(verts[i + 1 - exception], 1)
    sqrVertexArray.set(verts[8], 2)
    mesh.addPolygon(sqrVertexArray, mergeVerts, pointTolerance)
