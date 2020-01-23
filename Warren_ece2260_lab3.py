import numpy as np
import matplotlib.pyplot as plt


def find_time_constant(t, f_t):
    b = 0
    for ii in range(0, 10000):
        if((f_t[ii] - 3.16) < 0.00001):
            b = ii
    return t[b]

def main():
    t = np.linspace(0, 1, 100000)
    f_t = 5 - 5*np.exp(-1000*t)
    print(find_time_constant(t, f_t))


if __name__ == "__main__": 
    main()