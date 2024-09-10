import interpolation as erp
import numpy as np
import math as mt
import common as cm
r=mt.pi/2
x1=mt.cos(r/2)
q0=np.array([x1,mt.sin(r/2),0,0])

r=mt.pi/3
x1=mt.cos(r/2)
q1=np.array([x1,mt.sin(r/2),0,0])

r=mt.pi/6
x1=mt.cos(r/2)
q2=np.array([x1,mt.sin(r/2),0,0])

r=mt.pi
x1=mt.cos(r/2)
q3=np.array([x1,mt.sin(r/2),0,0])

q1star=cm.conjugate(q1)
q2star=cm.conjugate(q2)
    
s1=cm.GraBmann(q1,cm.Quat_Exp(-(cm.Quat_Log(cm.GraBmann(q1star,q0))+cm.Quat_Log(cm.GraBmann(q1star,q2)))*0.25))
s2=cm.GraBmann(q2,cm.Quat_Exp(-(cm.Quat_Log(cm.GraBmann(q2star,q1))+cm.Quat_Log(cm.GraBmann(q2star,q3)))*0.25))

for i in range(1,3):
    print(i)

#print(s2)