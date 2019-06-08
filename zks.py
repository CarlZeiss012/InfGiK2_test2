# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:12:23 2019

@author: Bartek
"""
from math import pi, sqrt, atan, sin, cos, tan
def dod(l):
    new_l = []
    cumsum = 0
    for elt in l:
        cumsum += elt
        new_l.append(cumsum)
    return new_l
def vin(oks,rks,gks,kks):
    f1= oks*pi/180
    l1=rks*pi/180
    f2=gks*pi/180
    l2= kks*pi/180
    a=6378137.000
    e2=0.00669438002290
    b=a*sqrt(1-e2)
    f=1-(b/a)
    Ua=atan((1-f)*tan(f1))
    Ub=atan((1-f)*tan(f2))
    dl=l2-l1
    L=dl
    i=0
    warunek=1
    while warunek > (0.000001/206265):
        i=i+1
        sd=sqrt(((cos(Ub)*sin(dl))**2)+(cos(Ua)*sin(Ub)-sin(Ua)*cos(Ub)*cos(dl))**2)
        cd=sin(Ua)*sin(Ub)+cos(Ua)*cos(Ub)*cos(dl)
        d=atan(sd/cd)
        sa=cos(Ua)*cos(Ub)*sin(dl)/sd
        c2a=1-sa**2
        c2d=cd-2*sin(Ua)*sin(Ub)/c2a
        C=(f/16)*c2a*(4+f*(4-3*c2a))
        Ls=L
        L=dl+(1-C)*f*sa*(d+C*sd*(c2d+C*cd*(-1+2*c2d**2)))
        warunek = abs(L-Ls)
    u2=((a**2-b**2)/b**2)*c2a
    A=1+(u2/16384)*(4096+u2*(-768+u2*(320-175*u2)))
    B=(u2/1024)*(256+u2*(-128+u2*(74-47*u2)))
    dd=B*sd*(c2d+(1/4)*B*(cd*(-1+2*(c2d**2))-(1/6)*B*c2d*(-3+4*(sd**2))*(-3+4*(c2d**2))))
    s=b*A*(d-dd)
    return s
