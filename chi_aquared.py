import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print loansData['Open.CREDIT.Lines']
print freq

chi, p = stats.chisquare(freq.values())

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
