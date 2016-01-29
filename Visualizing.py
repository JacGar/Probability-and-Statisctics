import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
loansData.hist(column='Amount.Requested')

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.figure()
loansData.boxplot(column='Amount.Funded.By.Investors')
loansData.hist(column='Amount.Funded.By.Investors')

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()
