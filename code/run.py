from code.Commons import the,cli

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


main()