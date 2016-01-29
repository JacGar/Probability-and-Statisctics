import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)
print c

count = sum(c.values())
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count))

plt.boxplot(x)
plt.savefig("box.png")

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("hist.png")

plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("QQ.png")
