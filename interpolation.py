import math as mt
import numpy as np
import common as cm
def Lerp(q0,q1,t):
    # calculate times of q1 and q2
    
    if(cm.qtimes(q0,q1)<0):
        q0=-q0
    
    qt=(1-t)*q0+t*q1
    return qt

def Nlerp(q0,q1,t):
    # calculate times of q1 and q2
    if(cm.qtimes(q0,q1)<0):
        q0=-q0
    
    
    qt=(1-t)*q0+t*q1
    
    # Normalization
    l=mt.sqrt(mt.pow(qt[0],2),mt.pow(qt[1],2),mt.pow(qt[2],2),mt.pow(qt[3],2))
    qt=qt/l
    return qt

def Slerp(q0,q1,t):
    if(cm.qtimes(q0,q1)<0):
        q0=-q0
    times=cm.qtimes(q0,q1)
    theta=mt.acos(times)
    if(theta<mt.pi*0.01):
        return Nlerp.Nlerp(q0,q1,t)
    
    else:
        sin_theta=mt.sin(theta)
        
        a=mt.sin((1-t)*theta)/sin_theta
        b=mt.sin(t*theta)/sin_theta
        
        qt=a*q0+b*q1
        return qt
    
def Slerp_Power(q0,q1,t):
    # qt=(q1 q0star)^t q0
    qt=cm.qtimes(mt.pow(cm.qtimes(q1,cm.conjugate(q0)),t),q0)
    return qt