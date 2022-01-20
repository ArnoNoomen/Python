
import sys
import os
import argparse
import functions as func

GLOBAL1 = 'hallo'

def functie1():
    print(GLOBAL1)

def functie2():
    GLOBAL1 = 'oke'  # geeft warning bij pylint

def main():

    parser = argparse.ArgumentParser(description='ZoekenVervang')
    parser.add_argument('--file', dest='file', action='store', help='inputfile opgeven', required=True)

    args = parser.parse_args()
    if not os.path.exists(args.file):
        print('Bestand {} bestaat niet'.format(args.file))
        sys.exit(1)

    print(GLOBAL1)
    functie1()
    functie2()
    functie1()
    print(func.substr('hallo', 2,2))

    with open(args.file, 'r') as fp1:
        for row in fp1:
            print('{}'.format(row.strip()))

if __name__ == '__main__':
    main()
