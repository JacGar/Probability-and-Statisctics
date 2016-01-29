import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
plt.savefig("Box Requested.png")
loansData.hist(column='Amount.Requested')
plt.savefig("Hist Requested.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("QQ Requested.png")
plt.figure()
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("Box Funded.png")
loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("Hist Funded.png")
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("QQ Funded.png")
