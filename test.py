import interpolation as erp
import numpy as np
import math as mt
import common as cm
r=mt.pi*0.5
x1=mt.cos(r/2)
q0=np.array([x1,0,mt.sin(r/2),0])

r=mt.pi/3
x1=mt.cos(r/2)
q1=np.array([x1,mt.sin(r/2),0,0])

print(erp.Slerp(q0,q1,0.4))
print(cm.mo(erp.Slerp(q0,q1,0.4)))
