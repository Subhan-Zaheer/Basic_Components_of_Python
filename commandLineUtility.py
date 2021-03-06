import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,  help="Enter a number. This a code for calculation of two numbers.")

    parser.add_argument('--y', type=float, default=5.0,  help="Enter a number. This a code for calculation of two numbers.")

    parser.add_argument('--o', type=str, default="",  help="Enter a operator for calculation. This a code for calculation of two numbers.")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))