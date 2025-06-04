# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 14:14:26 2025

@author: SSAFY
"""

import numpy as np

c = np.array([[0,1,2],[3,4,5]])
print(c)
print(len(c))
print(len(c[0]))


d = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])

three_d = np.array([[[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]],
                    [[11, 12, 13, 14],
                     [15, 16, 17, 18],
                     [19, 20, 21, 22]]])

print(len(three_d), len(three_d[0]), len(three_d[0][0]))

## 배열의 차원과 크기
print("배열의 차원 :", three_d.ndim)
print("배열의 크기 :", three_d.shape)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print(x[x % 3 == 0])
print(x[x % 4 == 1])
print(x[(x % 3 == 0) & (x % 4 == 1)])


