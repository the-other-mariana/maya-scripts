#File:      pool_MarianaAvalos2.py
#Date:      28/05/2019
#Name:      Mariana Avalos
#Description: code that creates a static or animated pool mesh

import maya.cmds as cmds
import math
import maya.OpenMaya as OM
import pymel.core as pm
DEFAULT = 5


# --------------- USER VARIABLES ----------------
animateMesh = True # choose True or False to animate mesh
frames = 20

# 12 18 13 25
height = 12
length = 18
rows = 13
cols = 25
waveHeight = 0.5
Nwaves = 1 # number of waves per row

# displacement: whether or not the even rows coincide with the odd rows
displacement = 0.0 # max is 1.0
#-------------------------------------------------

# -------------- VALIDATIONS ---------------
if frames <= 0:
    frames = DEFAULT
if height <= 0:
    height = DEFAULT
if length <= 0:
    length = DEFAULT
if rows <= 1:
    rows = DEFAULT
if cols <= 1:
    cols = DEFAULT
if waveHeight <= 0:
    waveHeight = 1.0
if Nwaves <= 0:
    Nwaves = DEFAULT
if displacement < 0.0 or displacement > 1.0:
    displacement = 1.0
    
frames = int(frames)
rows = int(rows)
cols = int(cols)
Nwaves = int(Nwaves)
# -------------------------------------------

# -------------- POOL FRAME FUNCTION ---------------
# function that adds pool frame only if mesh is animated
def createPoolFrame(poolVerts):
    quadArray = OM.MPointArray()
    quadArray.setLength(4)
    for p in range(0, 2):
        for j in range(0, 3):
            for i in range(0, 3):
                if p != 0:
                    quadArray.set(poolVerts[p][(i) + (j * (3 + 1))], 0)
                    quadArray.set(poolVerts[p][(i + (3 + 1)) + (j * (3 + 1))], 1)
                    quadArray.set(poolVerts[p][(i + (3 + 2)) + (j * (3 + 1))], 2)
                    quadArray.set(poolVerts[p][(i + 1) + (j * (3 + 1))], 3)
                    poolMesh.addPolygon(quadArray, mergeVerts, pointTolerance)
                else:
                    quadArray.set(poolVerts[p][(i) + (j * (3 + 1))], 0)
                    quadArray.set(poolVerts[p][(i + 1) + (j * (3 + 1))], 1)
                    quadArray.set(poolVerts[p][(i + (3 + 2)) + (j * (3 + 1))], 2)
                    quadArray.set(poolVerts[p][(i + (3 + 1)) + (j * (3 + 1))], 3)
                    poolMesh.addPolygon(quadArray, mergeVerts, pointTolerance)
            
    # array that has the following info:
    # [index1, index2, index3, increment]
    joins = [[0, 1, 2, 1], [3, 7, 11, 4], [15, 14, 13, -1], [12, 8, 4, -4]]
    
    quadArray = OM.MPointArray()
    quadArray.setLength(4)
    
    # following loop connects the outside faces from the frame
    for i in range(0, 4):
        for j in range(0, 3):
            quadArray.set(poolVerts[0][joins[i][j]], 0)
            quadArray.set(poolVerts[1][joins[i][j]], 1)
            quadArray.set(poolVerts[1][joins[i][j] + joins[i][3]], 2)
            quadArray.set(poolVerts[0][joins[i][j] + joins[i][3]], 3)
            poolMesh.addPolygon(quadArray, mergeVerts, pointTolerance)
            
    joins2 = [[5, 1], [6, 4], [10, -1], [9, -4]]
    
    # following loop connects the inside faces of the frame
    for j in range(0, 4):
        quadArray.set(poolVerts[0][joins2[j][0]], 0)
        quadArray.set(poolVerts[1][joins2[j][0]], 1)
        quadArray.set(poolVerts[1][joins2[j][0] + joins2[j][1]], 2)
        quadArray.set(poolVerts[0][joins2[j][0] + joins2[j][1]], 3)
        poolMesh.addPolygon(quadArray, mergeVerts, pointTolerance)
        
    # erases the middle faces of the frame for the middle space
    cmds.delete('polySurface1.f[4]')
    cmds.delete('polySurface1.f[12]')
# ----------------------------------------------------

# global calculations and variables
verts = []
mesh = OM.MFnMesh()
poolMesh = OM.MFnMesh()
mergeVerts = True
pointTolerance = 0.001

Pi = 3.1416
rs = (height * 1.00) / (rows * 1.00)
cs = (length * 1.00) / (cols * 1.00)
if animateMesh == True:
    rows += 2
lh = (length * 1.00) / 2.0
hh = (height * 1.00) / 2.0
zPos = waveHeight * 2.33
zNeg = -0.1
EPS = 0.2

# defining the pool frame points
poolVerts = [[OM.MPoint( -lh - 2*rs - EPS, zPos,  hh + 2*rs + EPS),
            OM.MPoint( -lh, zPos, hh + 2*rs + EPS),
            OM.MPoint( lh, zPos, hh + 2*rs + EPS),
            OM.MPoint( lh + 2*rs + EPS, zPos, hh + 2*rs + EPS),
            
            OM.MPoint( -lh - 2*rs - EPS, zPos, hh ),
            OM.MPoint( -lh, zPos, hh ),
            OM.MPoint( lh, zPos, hh ),
            OM.MPoint( lh + 2*rs + EPS, zPos, hh ),
            
            OM.MPoint( -lh - 2*rs - EPS, zPos, -hh ),
            OM.MPoint( -lh, zPos, -hh ),
            OM.MPoint( lh, zPos, -hh ),
            OM.MPoint( lh + 2*rs + EPS, zPos, -hh ),
            
            OM.MPoint( -lh- 2*rs - EPS, zPos, -hh - 2*rs - EPS),
            OM.MPoint( -lh, zPos, -hh - 2*rs - EPS),
            OM.MPoint( lh, zPos, -hh - 2*rs - EPS),
            OM.MPoint( lh + 2*rs + EPS, zPos, -hh - 2*rs - EPS)
            ],
            [OM.MPoint( -lh - 2*rs - EPS, zNeg,  hh + 2*rs + EPS),
            OM.MPoint( -lh, zNeg, hh + 2*rs + EPS),
            OM.MPoint( lh, zNeg, hh + 2*rs + EPS),
            OM.MPoint( lh + 2*rs + EPS, zNeg, hh + 2*rs + EPS),
            
            OM.MPoint( -lh - 2*rs - EPS, zNeg, hh ),
            OM.MPoint( -lh, zNeg, hh ),
            OM.MPoint( lh, zNeg, hh ),
            OM.MPoint( lh + 2*rs + EPS, zNeg, hh ),
            
            OM.MPoint( -lh - 2*rs - EPS, zNeg, -hh ),
            OM.MPoint( -lh, zNeg, -hh ),
            OM.MPoint( lh, zNeg, -hh ),
            OM.MPoint( lh + 2*rs + EPS, zNeg, -hh ),
            
            OM.MPoint( -lh- 2*rs - EPS, zNeg, -hh - 2*rs - EPS),
            OM.MPoint( -lh, zNeg, -hh - 2*rs - EPS),
            OM.MPoint( lh, zNeg, -hh - 2*rs - EPS),
            OM.MPoint( lh + 2*rs + EPS, zNeg, -hh - 2*rs - EPS)
            ]
            ]

if animateMesh == True:
    createPoolFrame(poolVerts)

x = 0
z = 0
y = 0
d = 0

# creates the verts for the main mesh (not animated)
for r in range(0, rows + 1):
    x = 0
    for c in range(0, cols + 1):
        if r % 2 == 1:
            d = Pi*displacement
        else:
            d = 0
        y = waveHeight * ((-1)**(r)) * math.sin( x * (Nwaves*1.0 / (length / (2*Pi))) - 0.5*Pi + d)
        temp = pm.dt.Point(x - ( (length*1.0) / 2.0 ), y + waveHeight, z - ( (height*1.0) / 2.0 ) -  int(animateMesh)*2 * rs)
        verts.append(temp)
        x += cs
    z += rs
    
quadArray = OM.MPointArray()
quadArray.setLength(4)

# connects the main mesh's verts
for j in range(0, rows):
    for i in range(0, cols):
        quadArray.set(verts[(i) + (j * (cols + 1))], 0)
        quadArray.set(verts[(i + (cols + 1)) + (j * (cols + 1))], 1)
        quadArray.set(verts[(i + (cols + 2)) + (j * (cols + 1))], 2)
        quadArray.set(verts[(i + 1) + (j * (cols + 1))], 3)
        mesh.addPolygon(quadArray, mergeVerts, pointTolerance)

x = 0
z = 0
y = 0
d = 0
cont = 0
map = []

# for each frame, creates a vertex array cointaining its next positions in time
# each vertex array is stored in map variable
for f in range(frames):
    verts = []
    x = 0
    z = 0
    y = 0
    cont = 0
    d = 0
    for row in range(0, rows + 1):
        x = 0
        for col in range(0, cols + 1):
            if row % 2 == 1:
                d = Pi*displacement
            else:
                d = 0
            y = waveHeight * ((-1)**(row)) * math.sin( x * (Nwaves*1.0 / (length / (2*Pi))) - 0.5*Pi + f + d)
            pt = pm.dt.Point(x - ( (length*1.0) / 2.0 ), y + waveHeight, z - ( (height*1.0) / 2.0 ) - int(animateMesh)*2 * rs)
            verts.append(pt)
            x += cs
            cont += 1
        z += rs
    map.append(verts)
        
print("map[1]", len(map[1]))
print(map)

x = 0
z = 0
y = 0
cont = 0

# sets in time line the corresponding vertex array in map
if animateMesh == True:
    obj = pm.ls(type='mesh')[1]
    vtx_list = [obj.vtx[i] for i in range(obj.numVertices())]
    
    for f in range(frames):
        pm.currentTime(f + 1, update = True)
        if (len(map[f]) == obj.numVertices()):
            obj.setPoints(map[f])
        pm.setKeyframe(vtx_list)





