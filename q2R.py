import numpy as np
import math as mt
import R2q
# q=[cos(θ/2),sin(θ/2)∗v] v是旋转轴 q是单位四元数
def q2R(q):
    a=q[0]
    b=q[1]
    c=q[2]
    d=q[3]
    R = np.array([[1-2*mt.pow(c,2)-2*mt.pow(d,2),2*b*c-2*a*d,2*a*c+2*b*d],
                  [2*b*c+2*a*d,1-2*mt.pow(b,2)-2*mt.pow(d,2),2*c*d-2*a*b],
                  [2*b*d-2*a*c,2*a*b+2*c*d,1-2*mt.pow(b,2)-2*mt.pow(d,2)]])
    return R

r=mt.pi*0.5
q1=mt.cos(r/2)
q=np.array([q1,mt.sin(r/2),0,0])

print(q2R(q))
print(q)
print(R2q.func(q2R(q)))