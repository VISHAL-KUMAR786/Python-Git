import argparse 
import sys

def clac(args):
    if args.o == 'add':
        return args.x + args.y
    if args.o == 'sub':
        return args.x - args.y if args.x > args.y else args.y - args.x
    if args.o == 'multi':
        return args.x * args.y
    if args.o == 'div':
        return args.x / args.y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="Enter first number ?")
    parser.add_argument('--y',type=float,default=1.0,help="Enter Secound number ?")
    parser.add_argument('--o',type=str,default='add',help="Enter Secound number ?")

    args = parser.parse_args()
    sys.stdout.write(str(clac(args)))

    pass