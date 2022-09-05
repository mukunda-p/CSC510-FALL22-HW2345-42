import math

#Return the 'p'-th thing from the sorted list 't'. 
def per(self,t,p):
    p=math.floor(((0.5 if p is None else p)*len(t))+0.5)
    return t[max(1,min(len(t,p)))]
