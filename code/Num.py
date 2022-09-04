import math,random

class Num:
    
    #'Num' summarizes the stream of numbers
    def __init__(self,c=0,s=str()):
        self.n=0
        self.at=c
        self.name=s
        self._has=dict()
        self.low=math.inf
        self.high=-math.inf
        self.isSorted=True
        if(len(s)>0 and s[-1]=='-'):
            self.w=-1
        else:
            self.w=1

    #Return kept numbers, sorted.
    def nums(self):
        if (not self.isSorted):
            dict(sorted(self._has, key=lambda item: item[0]))
        return self._has
            
        

    #Reservoir sampler. Keep atmost 'the[num]' numbers 
    # (if we run out of space delete something old at random and add new)
    def add(self,ele,pos=None):
        if ele!='?':
            self.n=self.n+1
            self.low=min(self.low,v)
            self.high=min(self.high,v)
            if ( len(self._has)<(the['nums']/self.n) ):
                pos=1+len(self._has)
            elif ( random.randint(0,2*(the['nums']/self.n)) < (the['nums']/self.n) ):
                pos=random.randint(0,(the['nums']/self.n))
            if pos!=None:
                self.isSorted=False
                self._has[pos]=int(v)
    
    
    

