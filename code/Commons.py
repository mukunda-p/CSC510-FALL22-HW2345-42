import math
import sys
import re as reg

the={'eg':'','dump':False,'file':'','help':False,'nums':512,'seed':10019,'seperator':','}

#parsing
def coerce(ele):
    if(reg.search(r'\d',ele)):
        return float(ele)
    return ele

#Return the 'p'-th thing from the sorted list 't'. 
def per(t,p):
    p=math.floor(((0.5 if p is None else p)*len(t))+0.5)
    return t[max(1,min(len(t),p))]

#converts t to string and print
def oo(t):
    str_t=str(t)
    print(str_t)
    return t

#Maths
#rnd function
def rnd(x,places=0):
    mult = math.pow(places or 2)
    return math.floor(x*mult+0.5)/mult 

#parse csv file to rows and cols
def csv(fileName):
    if(fileName==None or len(fileName.strip())==0):
        raise Exception("FILE NOT FOUNDED")
    rows=[]
    with open(fileName,'r',encoding='utf-8') as file:
        row_eles=file.readlines()
        for row_ele in row_eles:
            k=list(map(coerce,row_ele.split(',')))
            rows.append(k)
    return rows

def cli():
    args=sys.argv[1:]
    
    i=0
    if(len(args)<2):
        raise Exception("Not enough arguments")

    while i < len(args):

        if '-e' in args[i]:
            the['eg']=args[i+1]
        elif '-d' in args[i]:
            if(args[i+1].lower()=='false'):
                the['dump']=False
            else:
                the['dump']=True
        
        elif '-f' in args[i]:
            the['file']=args[i+1]
        
        elif '-n' in args[i]:
            the['nums']=int(args[i+1])
        
        elif '-h' in args[i]:
            if(args[i+1].lower()=='false'):
                the['help']=False
            else:
                the['help']=True

        elif '-s' in args[i] or '-seed' in args[i]:
            the['seed']=int(args[i+1])
        
        elif '-sep' in args[i] or '-S' in args[i]:
            the['seperator']=args[i+1]

        else:
            raise Exception("Not correct arguments")
        
        i=i+2
