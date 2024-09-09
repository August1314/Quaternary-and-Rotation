import numpy as np
import math as mt
def mo(q):
    return mt.sqrt(q[0]*q[0]+q[1]*q[1]+q[2]*q[2]+q[3]*q[3])
def GraBmann(q0,q1):
    a=q0[0]
    b=q0[1]
    c=q0[2]
    d=q0[3]
    
    e=q1[0]
    f=q1[1]
    g=q1[2]
    h=q1[3]
    
    vt=a*e-b*f+c*g+d*h
    v0=np.array([b,c,d])
    v1=np.array([f,g,h])
    vx=a*v0+e*v1+np.array([c*h-d*g,-b*h+d*f,b*g-c*f])
    
    qt=np.array([vt,vx[0],vx[1],vx[2]])
    return qt


def conjugate(q):
    qt=np.array([q[0],-q[1],-q[2],-q[3]])
    return qt

def qtimes(q0,q1):
    a=q0[0]
    b=q0[1]
    c=q0[2]
    d=q0[3]
    
    e=q1[0]
    f=q1[1]
    g=q1[2]
    h=q1[3]
    # calculate times of q1 and q2
    times=a*e+b*f+c*g+d*h
    return times


r=mt.pi*0.5
q1=mt.cos(r/2)
qa=np.array([q1,mt.sin(r/2),0,0])

r=mt.pi/3
q2=mt.cos(r/2)
qb=np.array([q2,0,mt.sin(r/2),0])



