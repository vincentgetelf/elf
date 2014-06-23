# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 15:20:06 2014

@author: Administrator
"""

#def foo():
 #   pass
#print issubclass(foo.__class__,object)
from numpy import*
a=arange(15).reshape(3,5)
a=array([[0,1,1,1,2],[2,3,4,5,6],[4,5,6,7,2]])
print a.shape
print a.ndim
print a.dtype.name
print a.itemsize
print a.size
print type(a)

b=zeros((3,4))
print b

c=ones((3,4,5),dtype=int16)
print c

d=empty((3,3))
print d
print d.dtype.name

print exp(a)

print sqrt(a)

e=a
print add(a,e)

f=arange(10)**4
print f



