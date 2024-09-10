import math as mt
import numpy as np
import interpolation as erp
import common as cm
def get_control_point(arrayq,n):
    arrays=[]
    arrays.append(arrayq[0])
    
    for i in range(1,n-1):
        qi=arrayq[i]
        qibefore=arrayq[i-1]
        qiafter=arrayq[i+1]
        if(cm.qtimes(qi,qibefore)<0):
            qibefore=-qibefore
        if(cm.qtimes(qi,qiafter)<0):
            qiafter=-qiafter
        qi_conj=cm.conjugate(qi)
        m0=cm.GraBmann(qi_conj,qibefore)
        m1=cm.GraBmann(qi_conj,qiafter)
        
        m0_log=cm.Quat_Log(m0)
        m1_log=cm.Quat_Log(m1)
        m_log_sum=m0_log+m1_log
        k=-0.25*m_log_sum
        k_exp=cm.Quat_Exp(k)
        arrays.append(cm.GraBmann(qi,k_exp))
        
    arrays.append(arrayq[n-1])
    return arrays

def Squad(q0,s1,s2,q3,t):
    qt=erp.Slerp(erp.Slerp(q0,q3,t),erp.Slerp(s1,s2,t),2*t*(1-t))
    return qt

def Squad_test(arrayq,t,n):
    arrays=get_control_point(arrayq,n)
    qt=[]
    for i in range(1,n):
        qt.append(Squad(arrayq[i-1],arrays[i-1],arrays[i],arrayq[i],0.4))
    
    for i in range(0,n-1):
        print(qt[i])

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
arrayq=[q0,q1,q2,q3]
Squad_test(arrayq,0.4,4)