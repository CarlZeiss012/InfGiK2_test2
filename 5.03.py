# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:12:19 2019

@author: Lenovo
"""

xa=input('podaj x punktu a:')
print(xa)
ya=input('podaj y punktu a:')
print(ya)
xb=input('podaj x punktu b:')
print(xb)
yb=input('podaj y punktu b:')
print(yb)
xp=input('podaj x punktu p:')
print(xp)
yp=input('podaj y punktu p:')
print(yp)


if xa.lstrip('-').replace('.','',1).isdigit():
    xa=float(xa)
else:
    print('to nie jest liczba')
if ya.lstrip('-').replace('.','',1).isdigit():
    ya=float(ya)
else:
    print('to nie jest liczba')
if xb.lstrip('-').replace('.','',1).isdigit():
    xb=float(xb)
else:
    print('to nie jest liczba')
if yb.lstrip('-').replace('.','',1).isdigit():
    yb=float(yb)
else:
    print('to nie jest liczba')
if xp.lstrip('-').replace('.','',1).isdigit():
    xp=float(xp)
else:
    print('to nie jest liczba')
if yp.lstrip('-').replace('.','',1).isdigit():
    yp=float(yp)
else:
    print('to nie jest liczba')


#xa=float(xa)
#xb=float(xb)
#xp=float(xp)
#ya=float(ya)
#yb=float(yb)
#yp=float(yp)


a=(xb-xa)*(yp-ya)-(xp-xa)*(yb-ya)
if a>0:
    print('punkt po prawej stronie')
if a<0:
    print('punkt po lewej stronie')
if a==0:
    print('punkt współliniowy')