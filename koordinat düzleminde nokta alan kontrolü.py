# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:16:32 2021

@author: sedat
"""

x1=int( input("noktanın x değerini giriniz"))
y1=int( input("noktanın y değerini giriniz"))

en=int(input("dikdörtgenin en değerini giriniz"))
boy=int(input("dikdörtgenin boy değerini giriniz"))

x2=int( input("dikdörtgenin sol alt x değerini giriniz"))
y2=int( input("dikdörtgenin sol alt y değerini giriniz"))


cnt=0

if(x1>x2 and x1<x2+en):
    cnt+=1
if(y1>y2 and y1<y2+boy):
    cnt+=1
    
if(cnt==2):
    print("nokta alanın içinde")
    
