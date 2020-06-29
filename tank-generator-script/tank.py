#File:      tank.py
#Author:    Mariana Avalos
#Date:      22/02/2019
#Description: Python code that makes a 3D tank

import maya.cmds as c
import math as math

# 8 tires
tireTranslation = [3, -3]
tireRadius = 1.25
for j in range(len(tireTranslation)):
    for i in range(4):
        name = 'c' + str(i + (j * 4) + 1)
        c.polyCylinder(r = tireRadius, sx = 20, sy = 1, n = 'c' + str(i + (j * 4) + 1))
        c.setAttr(name + '.rotateZ', 90)
        c.setAttr(name + '.scaleY', 0.8)
        c.setAttr(name + '.translateZ', i * (tireRadius * 2) - (tireRadius * 3))
        c.setAttr(name + '.translateX', tireTranslation[j])

# body made with the coolest for
body = 'body'
c.polyCube(sx = 4, sy = 2, sz = 1, d = 5.25, h = 3, w = 4, n = body)
c.setAttr(body + '.translateY', 0.5)
bodyRadius = 0.5
zFactor = [1, -1]
for j in range(len(zFactor)):
    for i in range(0, 15):
        rads = (360.0 / 8)*(3.1416 / 180)
        x = -1 * bodyRadius * math.cos(rads * (i % 5))
        z = zFactor[j] * bodyRadius * math.sin(rads * (i % 5))
        c.polyMoveVertex(body + '.vtx[' + str(i + 15 * j) + ']', tx = x)
        c.polyMoveVertex(body + '.vtx[' + str(i + 15 * j) + ']', tz = z)
        if i in (5, 6, 7, 8, 9):
            c.polyMoveVertex(body + '.vtx[' + str(i + 15 * j) + ']', tz = 3 * zFactor[j])

# head of tank
head = 'head'
headRadius = 0.5
c.polyCube(sx = 4, sy = 1, sz = 1, d = 3, h = 1.0, w = 4, n = head)
c.setAttr(head + '.translateY', 2.6)
c.setAttr(head + '.translateZ', -1)

for i in range(10, 20):
    rads = (360.0 / 8)*(3.1416 / 180)
    z = -1 * headRadius * math.sin(rads * (i % 5))
    c.polyMoveVertex(head + '.vtx[' + str(i) + ']', tz = z)
    if i in (10, 11, 12, 13, 14):
        c.polyMoveVertex(head + '.vtx[' + str(i) + ']', tz = 1)

# axis under head
axis = 'axis'
c.polyCylinder(r = 1.5, sx = 20, sy = 1, h = 0.5, n = axis)
c.setAttr(axis + '.translateY', 2)
c.setAttr(axis + '.translateZ', -1.1)

# gun making: even parts are length 2 and odd parts are length 0.5
heights = [2, 0.5]
t = 1
gunRadius = 0.25
for i in range(0, 4):
    name = 'gun' + str(i)
    c.polyCylinder(r = gunRadius, sx = 8, sy = 1, h = heights[i % 2], n = name)
    c.setAttr(name + '.translateY', 2.6)
    c.setAttr(name + '.translateZ', t)
    c.setAttr(name + '.rotateX', 90)
    # translating: my height / 2 + next height / 2
    t += heights[i % 2] / 2 + heights[(i + 1) % 2] / 2
    gunRadius += 0.1
