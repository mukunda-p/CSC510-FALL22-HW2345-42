from code.Commons import *
from code.Num import Num
from code.Sym import Sym
from code.Cols import Cols
from code.Row import Row 


class Data: 
    
    def __init__(self,src):
        self.cols=None
        self.rows=[]
        self.src=src
        if type(self.src) == str:
            self.src=csv(src)
            for row in self.src:
                self.add(row)
        else:
            for row in self.src:
                self.add(row)

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


    def stats(self,column,fun='mid'):
        if(column=='x'):
            showCols=self.cols.x
        if(column=='y'):
            showCols=self.cols.y
        t={}
        for i in showCols:
            if(type(i)==Num):
                if(fun=='mid'):
                    v=i.mid()
                elif(fun=='div'):
                    v=i.div()
            t[i.name]=v
        return t

        




            
        

        


        
