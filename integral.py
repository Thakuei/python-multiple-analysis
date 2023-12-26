# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:48:59 2023

@author: hakue
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
"""
from mpl_toolkits.mplot3d import Axes3D
from sympy.plotting import plot3d
"""

#日本語が打てるようにする
plt.rcParams['font.family'] = 'Meiryo'

#xのプロット範囲
x = np.linspace(-3, 3, 100)

#yのプロット範囲
y = np.linspace(-3, 3, 100)

#メッシュグリッド
X,Y = np.meshgrid(x,y)

#関数の定義　式を代入する
def func(x,y):
    return x**2-y**25

#z軸の定義
Z = func(X, Y)

#積分領域の提示
Zf = lambda y, x:(func(x, y))
xrange, yrange = integrate.dblquad(Zf, 1, 3, 2, 3)

#3Dプロットを作成
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(1, 1, 1, projection="3d")
ax.plot_surface(X ,Y ,Z , cmap="viridis")

# 軸ラベルの設定
ax.set_xlabel("x軸")
ax.set_ylabel("y軸")
ax.set_zlabel("f(x, y)")

#積分領域/式
x_range = "1<x<3"
y_range = "2<y<3"
formula = "∬(x^2-y^2)dxdy"

#グラフタイトル/積分の領域・式を挿入
ax.set_title("重積分散布図, 積分の値:" + str(round(xrange)),size=20)

fig.text(0.1, 0.3, "式:" + formula, size=20)
fig.text(0.1, 0.25, "ｘの積分範囲:" + x_range, size=20 )
fig.text(0.1, 0.2,  "yの積分範囲:" + y_range, size=20 )

# グラフを表示
plt.show()

