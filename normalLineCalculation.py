import numpy as np
import scipy.integrate as spi
import csv
import matplotlib.pyplot as plt
import seaborn as sns

n = 1000000
u = 10.0
sigma = 10.0
size = 1
width = 0.1
para = [0.1]

def getf(_x):
    res =  (np.exp((-0.5)*_x**2) / np.sqrt(2*np.pi))
    return res

# print(type(spi.quad(getf,1000, 1000+width)[0]))

normdata = [[_x,n*spi.quad(getf, _x-width/2, _x+width/2)[0]] for _x in np.arange(-6,6, 0.001)]

with open("normalLine.csv", "w") as csvFile:
    writer = csv.writer(csvFile, lineterminator='\r')
    for i in normdata:
        # print(i)
        writer.writerow(i)

x = []
y = []
with open("normalLine.csv", "r") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

normalLine =  sns.lineplot(x=x, y=y, color = "red")

plt.savefig("normalLine.pdf")