import numpy as np
import matplotlib.pyplot as plt

#estimates time constant tau by comparing to known voltage value
def find_time_constant(t, f_t):
    b = 0
    for ii in range(0, 10000):
        if((f_t[ii] - 3.16) < 0.00001):
            b = ii
    return t[b]

#plots the 
def plot():
    t = np.linspace(0, 0.005, 1000)
    f_t = 5 - 5*np.exp(-1000*t)
    plt.plot(t, f_t)
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (V)")
    plt.show()

def main():
    t = np.linspace(0, 1, 100000)
    f_t = 5 - 5*np.exp(-1000*t)
    print(find_time_constant(t, f_t))
    plot()

    

if __name__ == "__main__": 
    main()