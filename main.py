__expname__ = "U(-sqrt3_sqrt3)"

from utils import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
import scipy.integrate as spi

setseed(59)
width = 0.1


n = 1000000
u = 0
sigma = 1
para = [-np.sqrt(3),np.sqrt(3)]

step = 1
size = 0

# x = []
# y = []
# with open("normalLine.csv", "r") as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         x.append(float(row[0]))
#         y.append(float(row[1]))

while size <1000:
    size += step
    datas = [getdata(para, size, "uni") for _ in range(n)]

    for i in range(n):
        _data  = datas[i]
        _data = (np.sum(_data)-size*u)/np.sqrt(size)/sigma
        datas[i] = _data

    bins = np.arange(-6, 6+width, width)
    # sns.histplot(datas, bins = bins)
    # normalLine =  sns.lineplot(x=x, y=y, color = "red")

    distances = [(np.sum([(datas[_x]>=bins[i] and datas[_x]<bins[i+1]) for _x in range(n)])-(n*spi.quad(getf, bins[i],bins[i+1])[0]))**2 for i in range(len(bins)-1)]

    loss = np.sum(distances)/(len(bins)-1)
    print({f"{size} | {loss}"})
    loss = np.log(loss)
    with open(f"data/losses_{__expname__}.csv", "a") as csvFile:
        writer = csv.writer(csvFile, lineterminator="\r")
        writer.writerow([size, loss])

    
    # plt.savefig(f"pictures/resfigure_{__expname__}_size{size}.pdf")
    # plt.clf()


    if size == 100:
        step = step*10
    print(f"size is {size}")
        