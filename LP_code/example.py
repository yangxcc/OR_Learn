import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

a = 0
while a<0.05:
    c = np.array([0.05,0.27,0.19,0.185,0.185])
    A = np.diag([0,0.025,0.015,0.055,0.026])
    '''
    numpy.diag(array)函数，array是一个1维数组时，结果形成一个以一维数组为对角线元素的矩阵
    array是一个二维矩阵时，结果输出矩阵的对角线元素
    '''
    b = a*np.ones((5,1))
    Aeq = np.array([[1,1.01,1.02,1.045,1.065]])
    beq = np.array([1])

    res = optimize.linprog(-c,A,b,Aeq,beq)
    x = res.x
    Q = -res.fun
  #  print(Q)
    plt.plot(a,Q,'*')
    a = a+0.001
plt.xlabel('a')
plt.ylabel('Q')
plt.show()