import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

print "Getting data"
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#Line to help debugging when I am in a bad connection on the public transport
print "Data acquired"

loansData["Interest.Rate"] = loansData["Interest.Rate"].map(lambda x: round(float(x.rstrip("%"))/100,4))
loansData["Loan.Length"] = loansData["Loan.Length"].map(lambda x: float(x.rstrip("months")))
loansData["FICO.Score"] = loansData["FICO.Range"].map(lambda x:int(str(x).split("-")[0]))
# print loansData.head()

# plt.figure()
# p = loansData['FICO.Score'].hist()
# plt.show()

# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

# plt.show()


intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print "R^2 =", f.rsquared
print "p-values =", f.pvalues

loansData.to_csv('loansData_clean.csv', header = True, index = False)
