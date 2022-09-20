import math,random,sys
from code.Commons import per,the

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
    
    def __str__(self):
        return "{"+ f" n:{self.n}, at:{self.at+1}, name:{self.name}, low:{self.low}, high:{self.high}, isSorted:{self.isSorted}, w:{self.w}"+"}"

    #Return kept numbers, sorted.
    def nums(self):
        if (not self.isSorted):
            list(sorted(self._has))
        return self._has
            
        

    #Reservoir sampler. Keep atmost 'the[nums]' numbers 
    # (if we run out of space delete something old at random and add new)
    def add(self,ele,pos=None):
        if ele!='?':
            self.n=self.n+1
            self.low=min(self.low,int(ele))
            self.high=max(self.high,int(ele))
            if ( (len(self._has))<(the['nums']) ):
                pos=1+len(self._has)
            elif ( random.randint(0,sys.maxsize) < (the['nums']/self.n) ):
                pos=random.randint(0,len(self._has))
            if pos!=None:
                self.isSorted=False
                self._has[pos]=int(ele)


    #Diversity (standard deviation from Nums, entropy for Syms)
    def div(self):
        a=self.nums()
        return (per(a,0.9)-per(a,0.1))/2.58 
    
    #Central tendency (median for Nums, mode for Syms)
    def mid(self):
        return per(self.nums(),0.5) 





    
    
    

