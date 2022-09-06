import math

the={}

#Return the 'p'-th thing from the sorted list 't'. 
def per(t,p):
    p=math.floor(((0.5 if p is None else p)*len(t))+0.5)
    return t[max(1,min(len(t),p))]

#converts t to string and print
def oo(t):
    str_t=str(t)
    print(str_t)
    return t

