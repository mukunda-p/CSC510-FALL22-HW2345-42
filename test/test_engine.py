from code.Num import Num
from code.The import the
from code.common import *

def test_engine_num():
    num=Num()
    for i in range(1,101):
        num.add(i)
    mid,div=num.mid(),num.div()
    assert 50<=mid and mid<=52 and 30.5<div and div<32

def test_engine_bignum():
    num=Num()
    the['nums']=32
    for i in range(1,1001):
        num.add(i)
    oo(num.nums())
    assert len(num._has)==32
    
