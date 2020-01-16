
import numpy as np

def det_2x2 (A):
    # ad = np.multiply(A[0, 0], A[1, 1])
    # bc = np.multiply(A[0, 1], A[1, 0])
    # detA = ad - bc
    detA = (A[0, 0]*A[1, 1] - A[1, 0]*A[0, 1])
    return detA

def det_3x3 (A):
    aa = (A[0, 0]*((A[1, 1]*A[2, 2]) - (A[1, 2]*A[2, 1])))
    bb = (A[0, 1]*((A[1, 0]*A[2, 2]) - (A[2, 0]*A[1, 2])))
    cc = (A[0, 2]*((A[1, 0]*A[2, 1]) - (A[2, 0]*A[1, 1])))
    detA = aa - bb + cc
    return detA

def cramer_2x2(A,b):
    den = det_2x2(A)
    xnum = ((b[0, 0]*A[1, 1]) - (b[1, 0]*A[0, 1]))
    ynum = ((b[1, 0]*A[0, 0]) - (b[0, 0]*A[1, 0]))
    x = (xnum/den)
    y = (ynum/den)
    return (x,y)

def cramer_3x3(A,b):
    e = np.hstack((A,b))
    den = det_3x3(A)
    numx = det_3x3(e[:,[3,1,2]])
    numy = det_3x3(e[:,[0,3,2]])
    numz = det_3x3(e[:,[0,1,3]])
    x = (numx/den)
    y = (numy/den)
    z = (numz/den)
    return (x,y,z)
  
def main ():
    # set up a 2x2 array
    A = np.array ([[1. , 2. , 3.],
    [4. , 5. , 6.], [7. , 2. , 9.]])
    print(A)
    b = np. array ([[5.] , [6.] , [7]])
    print(b)
    print ( cramer_3x3 (A,b))
    # print (np. linalg . solve (A,b))

if __name__ == "__main__":
    main()