###############################################
# Name:Vasantha Gundeti
# Course:CMPS 5363 cryptography
# Date:4 August 2015
# Program 3:Elliptical Curve Encryption
###############################################
import argparse
import sys
import math
import plotcurve as c
import fractions

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--scalar", dest="a", help="Given y^2 = x^3 + a*x + b: Input 'a'")
    parser.add_argument("-b", "--constant", dest="b", help="Given y^2 = x^3 + a*x + b: Input 'b'")
    parser.add_argument("-x1", "--firstXValue", dest="x1", help="Given P1(x1,y1): Input x1")
    parser.add_argument("-y1", "--firstYValue", dest="y1", help="Given P1(x1,y1): Input y1")
    parser.add_argument("-x2", "--secondXValue", dest="x2", help="Given P2(x2,y2): Input x2")
    parser.add_argument("-y2", "--secondYValue", dest="y2", help="Given P1(x2,y2): Input y2")
    args = parser.parse_args()
    print("a=", args.a, "b=", args.b, "x1=", args.x1, "y1=", args.y1, "x2=", args.x2, "y2=", args.y2)
	
    a = fractions.Fraction(args.a)
    b = fractions.Fraction(args.b)
    x1 = fractions.Fraction(args.x1)
    x2 = fractions.Fraction(args.x2)
    y1 = fractions.Fraction(args.y1)
    y2 = fractions.Fraction(args.y2)
    print("Elliptical Curve Equation:y^2 = x^3 +", a, "* x +", b)
    p=pow((pow(x1,3) + a*x1 + b),(1/2))
    q=pow((pow(x2,3) + a*x2 + b),(1/2))
    
	#Checking whether given points lie on curve
    if p!=y1 and q!=y2 :
        print("Given points are on curve")
    else:
        print("Given points are not on the curve")    
    
	#checking whether x and y coordinates of different points are equal
	#if coordinates are equal goes to if condition and finds slope value or else find the point slope value
    if x1 == x2 and y1 == y2:
        m = (3 *pow(x1,2) + a) / (2 * y1)
    else:
        m = (y1-y2)/(x1-x2)
    
   
    x3 = fractions.Fraction(pow(m,2) - x1 - x2).limit_denominator(1000)
    y3 = fractions.Fraction(y1 + m * (x3-x1)).limit_denominator(1000)
    print("New coordinates are:",x3,y3)
	
	#checking whether third point lie on curve
    r=pow((pow(x3,3) + a*x3 + b),(1/2))
    if  r!= y3:
        print("new point is not on the curve")
    else:
        print("new point is on the curve")

    max_val=max(abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3))
    w=max_val+10
    h=max_val+12
	
	#plotting the graph
    c.plotcurve(w,h,x1,y1,x2,y2,m,x3,y3,a,b)
    
if __name__ == '__main__':
    main()
