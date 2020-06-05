# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:46:27 2020

@author: jeevan
"""

def jk_similarity(arr1,arr2):
    try:
        intscore= sum([(a*b) for a, b in zip(arr1, arr2)])
        ans=(intscore/sum(arr1))
        if(ans>1):
            return 1.0
        else:
            return ans
    except ZeroDivisionError:
        return 1.0
        