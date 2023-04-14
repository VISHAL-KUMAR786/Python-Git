'''
step of argparse 
1. Import the Python argparse module
2. Create the parser
3. Add optional and positional arguments to the parser
4. Execute .parse_args()

.parse_args(), we will get the Namespace object that contains a simple property for each input argument received from the command line
'''
import argparse
import sys

def calc(args):
    if args.o == 'add':
        # print("Sum of two number is ") this is also working in writing in termainl
        return args.a + args.b 
    elif args.o == 'sub':
        # print("Subtraction of two number is ")
        if (args.a > args.b ):
            return f"Subtraction of two number is {args.a - args.b}"
        else:
            return  f"Subtraction of two number is {args.b - args.a}"        
    elif args.o == 'multi':
        # print("Multiplication of two number is ")
        return f"Multiplication of two number is {args.a * args.b }"
    elif args.o == 'div':
        # print("Division of two number is ")
        return f"Division of two number is {args.a / args.b }"
    else:
        return "please enter a valid input"


if __name__ == '__main__':
    parser = argparse.ArgumentParser() # main the object of argparse
    parser.add_argument('--a',type=float,default=1.0,help="Enter first number")
    parser.add_argument('--b',type=float,default=1.0,help="Enter Secound number")
    parser.add_argument('--o',type=str,default='add',help="Enter Operator")

    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))
