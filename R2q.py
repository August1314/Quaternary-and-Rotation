import numpy as np
import math as mt
# q=[cos(θ/2),sin(θ/2)∗v] v是旋转轴 q是单位四元数
def func(R):
    ax=R[0][0]
    ay=R[0][1]
    az=R[0][2]
    bx=R[1][0]
    by=R[1][1]
    bz=R[1][2]
    cx=R[2][0]
    cy=R[2][1]
    cz=R[2][2]
    
    q1=0.5*mt.sqrt(1+ax+by+cz)
    q2=0.5*np.sign(bz-cy)*mt.sqrt(ax-by-cz+1)
    q3=0.5*np.sign(cx-az)*mt.sqrt(-ax+by-cz+1)
    q4=0.5*np.sign(ay-bx)*mt.sqrt(-ax-by+cz+1)
    
    q=np.array([q1,q2,q3,q4])
    return q