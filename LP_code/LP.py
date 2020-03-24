import numpy as np
from scipy import optimize

'''
这是线性规划的标准形式，当使用linprog()函数求的是函数的最小值
min z = -7x1+7x2-2x3-x4-6x5

       3x1-x2+x3-2x4=-3
s.t.=  2x1+x2+x4+x5=4
       -x1+3x2-3x4+x6=12
       xi>=0
'''

c = np.array([-7,7,-2,-1,-6,0])
a = np.array([[3,-1,1,-2,0,0],[2,1,0,1,1,0],[-1,3,0,-3,0,1]])
b = np.array([-3,4,12])

res = optimize.linprog(c,A_eq=a,b_eq=b)

print("决策变量的值为：")
print(res.x)
print("目标函数的最小值是")
print('%.2f'%res.fun)
