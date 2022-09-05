import math,random
from The import the
from Commons import per

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
            
        

    #Reservoir sampler. Keep atmost 'the[nums]' numbers 
    # (if we run out of space delete something old at random and add new)
    def add(self,ele,pos=None):
        if ele!='?':
            self.n=self.n+1
            self.low=min(self.low,int(ele))
            self.high=max(self.high,int(ele))
            if ( len(self._has)<(the['nums']) ):
                pos=1+len(self._has)
            elif ( random.randint(0,2*(the['nums']/self.n)) < (the['nums']/self.n) ):
                pos=random.randint(0,(the['nums']/self.n))
            if pos!=None:
                self.isSorted=False
                self._has[pos]=int(ele)


    #Diversity (standard deviation from Nums, entropy for Syms)
    def div(self,a):
        a=self.nums()
        return (per(a,0.9)-per(a,0.1))/2.58 
    
    #Central tendency (median for Nums, mode for Syms)
    def mid(self):
        return per(self.nums(),0.5) 





    
    
    

