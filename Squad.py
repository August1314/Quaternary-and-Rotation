import math as mt
import numpy as np
import interpolation as erp
import common as cm
def Squad(q0,q1,q2,q3,t):
    if(cm.qtimes(q0,q1)<0):
        q0=-q0
    
    q1star=cm.conjugate(q1)
    q2star=cm.conjugate(q2)
    
    s1=q1*mt.exp(-(mt.log(cm.qtimes(q1star,q0))+mt.log(cm.qtimes(q1star,q2)))*0.25)
    s2=q2*mt.exp(-(mt.log(cm.qtimes(q2star,q1))+mt.log(cm.qtimes(q2star,q3)))*0.25)
    print(s1)
    print(s2)
    qt=erp.Slerp(erp.Slerp(q1,q2,t),erp.Slerp(s1,s2,t),2*t*(1-t))
    return qt


r=mt.pi*0.5
x1=mt.cos(r/2)
q0=np.array([x1,0,mt.sin(r/2),0])

r=mt.pi/3
x1=mt.cos(r/2)
q1=np.array([x1,mt.sin(r/2),0,0])

r=mt.pi/6
x1=mt.cos(r/2)
q2=np.array([x1,mt.sin(r/2),0,0])

r=mt.pi
x1=mt.cos(r/2)
q3=np.array([x1,mt.sin(r/2),0,0])

print(Squad(q0,q1,q2,q3,0.4))