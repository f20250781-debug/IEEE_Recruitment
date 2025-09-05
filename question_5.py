# MatPlotLib
import numpy as np # Imports numpy library
import matplotlib.pyplot as plt # Imports pyplot from matplotlib library
mean = 0 # Defining mean of normal distribution
std = 1 # Defining the Standard Deviation of normal distribution 
size = 1000 # Defines size of distribution (1000 elements)
n_distr = np.random.normal(mean,std,size) # Generates a normal distribution with defined parameters
#n_distr = np.sort(n_distr)
x = np.arange(0,1000) # Defines range of our x-axis
plt.scatter(x, n_distr) # Defines values to plot on x and y axes
plt.title("Normal Distribution Graph") # Title of plot
plt.xlabel("Value") # Label for x-axis

plt.ylabel("Frequency")
plt.show()