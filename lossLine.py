import matplotlib.pyplot as plt
import seaborn as sns
import csv
import numpy as np

x,y = [],[]
with open("data/losses_E(0.1).csv","r") as csvFile:
    reader = csv.reader(csvFile)
    for _i in reader:
        x.append(float(_i[0]))
        y.append(float(_i[1]))

# x = x[:30]
# y = y[:30]
sns.lineplot(x=x,y=y, label = "exp", color = "blue")

x,y = [],[]
with open("data/losses_U(-sqrt3_sqrt3).csv","r") as csvFile:
    reader = csv.reader(csvFile)
    for _i in reader:
        x.append(float(_i[0]))
        y.append(float(_i[1]))
sns.lineplot(x=x,y=y, label = "uni", color = "red")

x,y = [],[]
with open("data/losses_B(100_0.3).csv","r") as csvFile:
    reader = csv.reader(csvFile)
    for _i in reader:
        x.append(float(_i[0]))
        y.append(float(_i[1]))
sns.lineplot(x=x,y=y, label = "bern", color = "green")

x,y = [],[]
with open("data/losses_P(5).csv","r") as csvFile:
    reader = csv.reader(csvFile)
    for _i in reader:
        x.append(float(_i[0]))
        y.append(float(_i[1]))
sns.lineplot(x=x,y=y, label = "pois", color = "purple")

plt.legend()
plt.savefig("data/lossLines.pdf")
