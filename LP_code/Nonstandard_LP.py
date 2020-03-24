'''
max z = 2x1 + 3x2 − 5x3

s.t. x1+x2+x3=7
    2x1−5x2+x3>=10
    x1+3x2+x3<=12
    x1,x2,x3>=0
'''

import numpy as np
from scipy import optimize

c = np.array([2,3,-5])
a = np.array([[-2,5,-1],[1,3,1]])   #注意这里是-2，5，-1
b = np.array([-10,12])
Aeq = np.array([[1,1,1]])
beq = np.array([7])

res = optimize.linprog(-c,a,b,Aeq,beq,bounds=((0,None),(0,None),(0,None)))   #注意这里是-c，因为是求最大值
# scipy.linprog这个函数，有一个bound参数，用来确定自变量的边界

print(res)