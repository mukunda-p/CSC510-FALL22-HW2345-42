import math
import csv

the={'seperator':',', 'nums': 512 , 'show_help': False, 'seed': 10019}

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

#Parse ‘the‘ config settings from ‘help‘.
def csv(fileName):
    if(fileName!=null or len(filename.strip())==0):
        raise Exception("FILE NOT FOUNDED")
    rows=[]
    with open(fileName,'r',encoding='utf-8') as file:
        row_ele=csv.reader(fileName,delimeter=the['seperator']
        rows.append(row_ele)
    return rows                      
