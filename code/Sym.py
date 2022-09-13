import math 

class Sym:
    def __init__(self,c=0,s='') -> None:
        self.n = 0
        self.name=s
        self.at=c
        self._has = dict()

    
    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self._has[v] = 1 + self._has.get(v, 0)


    def mid(self):
        return max(self._has, key=self._has.get)
    

    def div(self):
        fun = lambda p : p*math.log(p,2)
        e = 0  
        for key in self._has.keys():
            if self._has[key] > 0 :
                e = e - fun(self._has[key]/self.n)
        
        return e