# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:56:39 2023

@author: hakue
"""

import matplotlib.pyplot as plt
import matplotlib.patches as pat
"""
import numpy as np
import math
"""

fig = plt.figure(figsize=(6,6))

ax = fig.add_subplot(111)
"""
ax.grid(axis = "both")
"""
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

C = pat.Circle(xy = (0, 0), radius = 1.1, color = "black") #真ん中の丸
C1 = pat.Circle(xy = (-1.207, 1.207),radius=0.7, color = "black") #左耳
C2 = pat.Circle(xy = (1.207, 1.207),radius=0.7, color = "black") #右耳
C3 = pat.Ellipse(xy = (0, -0.1), width = 0.5,height=0.3, edgecolor = "white", facecolor = "black") #鼻
C4 = pat.Ellipse(xy = (0.35, 0.35), width = 0.3, height = 0.6, color = "white") #右目
C5 = pat.Ellipse(xy = (-0.35, 0.35), width = 0.3, height = 0.6, color = "white") #左目
C6 = pat.Ellipse(xy = (0.35, 0.25), width = 0.3, height = 0.4, edgecolor = "white", facecolor = "black") #右目中の黒
C7 = pat.Ellipse(xy = (-0.35, 0.25), width = 0.3, height = 0.4, edgecolor = "white", facecolor = "black") #左目中の黒
C8 = pat.Arc(xy = (-0.9, 0), theta1=270, theta2=320, width = 1, height = 1, edgecolor = "white") #C8~C10は口
C9 = pat.Arc(xy = (0.9, 0), theta1=220, theta2=270, width = 1, height = 1, edgecolor = "white")
C10 = pat.Arc(xy = (0, -0.05), theta1=210, theta2=331, width = 2, height = 1.3, edgecolor = "white")

#それぞれを表示させるための物
ax.add_patch(C)
ax.add_patch(C1)
ax.add_patch(C2)
ax.add_patch(C3)
ax.add_patch(C4)
ax.add_patch(C5)
ax.add_patch(C6)
ax.add_patch(C7)
ax.add_patch(C8)
ax.add_patch(C9)
ax.add_patch(C10)

#最後にこれを書いて図を表示させる
plt.show()


