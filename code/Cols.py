from code.Num import Num
from code.Sym import Sym

class Cols:

    def __init__(self,names):
        self.names=names
        self.all=[]
        self.klass=None
        self.x=[]
        self.y=[]

        for column_name in self.names:
            if column_name[0].isupper():
                column=Num(names.index(column_name),column_name)
            else:
                column=Sym(names.index(column_name),column_name)
            
            if column_name[-1]!=':':
                if('!' in column_name or '+' in column_name or '-' in column_name):
                    self.y.append(column)
                else:
                    self.x.append(column)

            if column_name[-1]=='!':
                self.klass=column
            self.all.append(column)
    
    def __str__(self):
        return f"names is {self.names}, all is {self.all}, klass is {self.klass}, x is {self.x}, y is {self.y}"