from http.client import MOVED_PERMANENTLY
import random
import seaborn; seaborn.set()
import pandas as pd
import numpy as np
from sqlalchemy import false, true
n=0
first=[]
second=[]
third=[]
fourth=[]
fifth=[]
sixth=[]
seventh=[]
Data=[first,second,third,fourth,fifth,sixth,seventh]
class Red:
    def __init__(self,money,people) :
        self.money=money
        self.people=people
        self.remainmoney=money
        self.remainpeople=people
        self.data=[]

    def RedEnvelop(self):
        r=random.random()
        min=0.01
        if self.remainpeople>1:
            max=self.remainmoney/self.remainpeople*2
            money=r*max
            money=round(money,2)
            if money<min:
                money=min
            self.remainpeople=self.remainpeople-1
            self.data.append(money)
            self.remainmoney=self.remainmoney-money

            return None
        if self.remainpeople<=1:
            self.data.append(round(self.remainmoney,2))
            self.remainpeople=self.remainpeople-1
            return None
        
    
    def ifnotempty(self):
        if self.remainpeople!=0:
            return true
        else:
            return false
List1=list()
List2=list()
List3=list()
List4=list()
List5=list()
List6=list()
List7=list()
List8=list()
List9=list()
for i in List1:
    List2.append(i[0])
print(np.mean(List2))
for i in List1:
    List3.append(i[1])
print(np.mean(List3))
for i in List1:
    List4.append(i[2])
print(np.mean(List4))
for i in List1:
    List5.append(i[3])
print(np.mean(List5))
for i in List1:
    List6.append(i[4])
print(np.mean(List6))
for i in List1:
    List8.append(i[5])
print(np.mean(List8))

for i in List1:
    List7.append(i[6])
print(np.mean(List7))
while n<=100000:
    test=Red(5,7)
    rank=0
    while test.remainpeople!=0:
        test.RedEnvelop()
    while rank<=6:
        Data[rank].append(test.data[rank])
        rank+=1
    n+=1
    List1.append(test.data)
List1
variance=0
for i in List2:
    variance=variance+(np.mean(List7)-i)**2
print(variance/100000)