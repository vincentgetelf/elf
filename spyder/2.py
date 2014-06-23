# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 16:07:18 2014

@author: Administrator
"""

import math
import random
import numpy 
from scipy import weave
#help(math)
#help(random)
#help(numpy)
#内建apply函数调用函数
def function(a,b):
    print a,b
    
apply(function,("hello ","world"))
apply(function,(1,3+5))

apply(function,(),{"a":"s1","b":"s2"})

#type函数

def typeout(value):
    print type(value),value

typeout(1)
typeout("i")


