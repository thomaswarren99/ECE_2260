##
## Thomas Warren, 2020
## thomaswarren_lab1
## File description: Quadratic formula, factorials, and riemann sums
## functions_ece2260
##


import cmath
import math

# Calculates roots of coefficients using quadratic formula
def calculate_roots(coef):
    a = coef[0]
    b = coef[1]     #variables for the quadratic function
    c = coef[2]

    
    p = (-b + cmath.sqrt((b**2) - 4 * a * c))/(2 * a)    #pos and neg roots
    q = (-b - cmath.sqrt((b**2) - 4 * a * c))/(2 * a)
    
    roots = (p,q)
    return roots

# Calculates factorial of input n
def compute_factorial(n):
    b = 1
    for ii in range(1, n + 1):
        b = b * ii
    return b
    
    
# sums up factorials using the compute_factorial for each input n
def sum_factorial(n):
    a = 0
    for i in range(1, n+1):
        a += compute_factorial(i)
    return a

# the formula of the function used on the y-axis in the riemann sums
def f_x(x):
    a = (math.exp(-3*(x))) * math.cos((math.pi) * (x))
    return a

# function used to calculate the left riemann sum with 
# three inputs delta_x, lb, ub
def left_riemann(delta_x, lb, ub):
    # to do
    d = int(ub/delta_x)
    su = 0
    for i in range(lb, d):
        inc = delta_x * i
        a = f_x((inc)) * delta_x
        su += a
    return su

# function used to calculate the right riemann sum with 
# three inputs delta_x, lb, ub
def right_riemann(delta_x, lb, ub):
    d = int(ub/delta_x)
    su = 0
    for i in range(lb, d):
        inc = delta_x * (i + 1)
        a = f_x(inc) * delta_x
        su += a
    return su

    
# function finds the riemann sum by using the midpoint method with 
# inputs delta_x, lb, ub
def midpoint_riemann(delta_x, lb, ub):
    d = int(ub/delta_x)
    su = 0
    for i in range(lb, d):
        inc = delta_x * i
        mid = (inc + (inc + delta_x))/2
        a = delta_x * f_x(mid)
        su += a
    return su


# function finds the riemann sum by using the trapezoid method with 
# inputs delta_x, lb, ub    

def trap_riemann(delta_x, lb, ub):
    d = int(ub/delta_x)
    su = 0
    for i in range(lb, d):
        inc = i * delta_x
        a = delta_x * ((f_x(inc) + f_x(inc + delta_x))/2)
        su += a
    return su

    
def main():

    ##############################################################
    # Part 1
    ##############################################################
    print("Part 1 Results")
    
    coef = [2, 4, 0]
    roots = calculate_roots(coef)
    print("roots 1:")
    print(roots)

    coef = [1, 4, 4]
    roots = calculate_roots(coef)
    print("roots 2:")
    print(roots)
    
    coef = [1, 0, 9]
    roots = calculate_roots(coef)
    print("roots 3:")
    print(roots)

    coef = [2, 8, 26]
    roots = calculate_roots(coef)
    print("roots 4:")
    print(roots)

    ##############################################################
    # Part 2
    ##############################################################
    print("\n")
    print("Part 2 Results")
    
    for n in [4, 10, 16]:
        output_factorial = compute_factorial(n)
        print("computed factorial for n=%i is: %i" %
              (n, output_factorial))

    ##############################################################
    # Part 3
    ##############################################################
    print("\n")
    print("Part 3 Results")
    
    for n in [3, 5, 6]:
        output_summation = sum_factorial(n)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
        
    #############################################################
    # Part 4
    #############################################################
    print("\n")
    print("Part 4 Results")
    
    lb = 0
    ub = 10
    
    print("calculating left Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = left_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating right Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = right_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating midpoint Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = midpoint_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating trapezoid Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = trap_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

        
if __name__ == "__main__":
    main()
