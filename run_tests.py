from code.Commons import the,cli
from test.test_engine import *

def main():
    cli()

    if the['help']:
        print('''OPTIONS:
        -e --eg start-up example = test case can be passed to run
        -d --dump on test failure, exit with stack dump = false
        -f --file file with csv data = ../data/auto93.csv   
        -h --help show help = false
        -n --nums number of nums to keep = 512
        -s --seed random number seed = 10019
        -S --seperator feild seperator = ,]]''')
    
    if 'sym' in the['eg'].lower():
        test_engine_sym()
    elif 'num' in the['eg'].lower():
        test_engine_num()
    elif 'csv' in the['eg'].lower():
        test_engine_csv()
    elif 'add' in the['eg'].lower():
        test_engine_add()
        
        

main()