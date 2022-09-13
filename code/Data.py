from Commons import *
from Num import Num
from Sym import Sym
from Cols import Cols
from Row import Row 


class Data: 
    
    def __init__(self,src):
        self.cols=None
        self.rows={}
        if type(self.src) == str:
            self.src=csv(src)
            for row in src:
                self.add(row)
        else:
            for row in src:
                self.add(row)
    
## Data Add a ‘row‘ to ‘data‘. Calls ‘add()‘ to updatie the ‘cols‘ with new values.
    def add(self,xs):
        if not self.cols:
            self.cols=Cols(xs)
        else:
            if type(xs)!= Row:
                row=Row(xs)
            else:
                row=xs
            self.rows.append(row)
            for i in [self.cols.x,self.cols.y]:
                for j in i:
                    j.add(row.cells[j.at])

# For ‘showCols‘ (default=‘data.cols.x‘) in ‘data‘, show ‘fun‘ 
    def stats(self,fun='mid'):
        showCols=self.cols.x or self.cols.y
        t={}
        for i in showCols:
            if(type(i)==Num)
            if(fun=='mid'):
                v=i.mid()
            elfi(fun=='div'):
                v=i.div()
            t[i.name]=v
        return t

        




            
        

        


        
