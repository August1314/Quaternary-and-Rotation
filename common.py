import numpy as np
import math as mt
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

def cross(q0,q1):
    a=q0[0]
    b=q0[1]
    c=q0[2]
    d=q0[3]
    
    e=q1[0]
    f=q1[1]
    g=q1[2]
    h=q1[3]
    
    x1=a*e-b*f-c*g-d*h
    x2=c*h-d*g+a*f+e*b
    x3=d*f-b*h+a*g+e*c
    x4=b*g-c*f+a*h+e*d
    return np.array([x1,x2,x3,x4])

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

def reverse(q):
    mo2=mo(q)*mo(q)
    qstar=conjugate(q)
    qt=qstar/mo2

# Assuming q = [cos_a,sin_a*v]
def get_theta(q0):
    a=q0[0]
    b=q0[1]
    c=q0[2]
    d=q0[3]
    sin_a=mt.sqrt(b*b+c*c+d*d)
    cos_a=q0[0]
    theta=mt.asin(sin_a)
    return theta
    
def Quat_Log(q0):
    theta=get_theta(q0)
    q=np.array([0,theta*q0[1],theta*q0[2],theta*q0[3]])
    return q


# Assuming q = [0,theta*v]
def Quat_Exp(q):
    theta=mo(q)
    cos_a=mt.cos(theta)
    sin_a=mt.sin(theta)
    qt=q
    if(cos_a>0.9995):
        qt=conjugate(q)
    else:
        qt=q*sin_a/theta
    qt[0]=cos_a
    return qt
    




