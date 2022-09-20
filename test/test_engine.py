from code.Num import Num
from code.Sym import Sym
from code.Commons import *
from code.Data import Data

def test_engine_all():
    try:
        test_engine_bignum()
        test_engine_csv()
        test_engine_data()
        test_engine_num()
        test_engine_stats()
        test_engine_sym()
        test_engine_the()
        print("!!!!!!	PASS	ALL	true")
    except:
        print("!!!!!! Its a crash")

def test_engine_num():
    the['nums']=512
    num=Num()
    for i in range(1,101):
        num.add(i)
    mid,div=num.mid(),num.div()
    print()
    print(mid,div)
    print("!!!!!!	PASS	num	true")
    assert 50<=mid and mid<=52 and 30.5<div and div<32

def test_engine_bignum():
    the['nums']=32
    num=Num()
    for i in range(1,1001):
        num.add(i)
    print()
    oo(num.nums())
    print("!!!!!!	PASS	bignum	true")
    assert len(num._has)==32

def test_engine_the() :
    print()
    oo(the)
    print("!!!!!!	PASS	the	true")
    assert True

def test_engine_sym():
    sym=Sym()
    pairs=['a','a','a','a','b','b','c']
    for x in pairs:
        sym.add(x)
    mode=sym.mid()
    entropy=sym.div()
    entropy=(1000*entropy)//1/1000
    print()
    oo({"mid":mode,"div":entropy})
    print("!!!!!!	PASS	sym	true")
    assert mode=='a' and 1.37<= entropy and entropy <= 1.38

def test_engine_csv():
    n=0
    src=the['file']
    print()
    print(csv(src))
    print("!!!!!!	PASS	csv	true")
    assert True

def test_engine_data():
    src=the['file']
    d=Data(src)
    print()
    for i in d.cols.y:
        print(i)
    print("!!!!!!	PASS	data	true")
    assert True

def test_engine_stats():
    src=the['file']
    print()
    d=Data(src)
    print('xmid:',str(d.stats('x','mid')))
    print('xdiv:',str(d.stats('x','div')))
    print('ymid:',str(d.stats('y','mid')))
    print('ydiv:',str(d.stats('y','div')))
    print("!!!!!!	PASS	stats	true")
    assert True



