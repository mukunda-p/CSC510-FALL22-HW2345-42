from code.Num import Num
from code.The import the
from code.Sym import Sym
from code.common import *

def test_engine_num():
    the['nums']=512
    num=Num()
    for i in range(1,101):
        num.add(i)
    mid,div=num.mid(),num.div()
    assert 50<=mid and mid<=52 and 30.5<div and div<32

def test_engine_bignum():
    the['nums']=32
    num=Num()
    for i in range(1,1001):
        num.add(i)
    oo(num.nums())
    assert len(num._has)==32

def the () :
    oo(the)
    assert true

def test_engine_sym():
    sym=Sym()
    pairs=['a','a','a','a','b','b','c']
    for x in pairs:
        sym.add(x)
        mode=sym.mid()
        entropy=sym.div()
        entropy=(1000*entropy)//1/1000
        oo({"mid":mode,"div":entropy})
    assert mode=='a' and 1.37<= entropy and entropy <= 1.38



    
