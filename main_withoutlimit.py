from http.client import MOVED_PERMANENTLY
import random

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
            max=self.remainmoney
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

while n<=10000:
    test=Red(5,7)
    rank=0
    while test.remainpeople!=0:
        test.RedEnvelop()
    while rank<=6:
        Data[rank].append(test.data[rank])
        rank+=1
    n+=1
print(Data[0])