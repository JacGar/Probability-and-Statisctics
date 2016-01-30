import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData["Interest.Rate"] = loansData["Interest.Rate"].map(lambda x: round(float(x.rstrip("%"))/100,4))
loansData["Loan.Length"] = loansData["Loan.Length"].map(lambda x: float(x.rstrip("months")))
loansData["FICO.Score"] = loansData["FICO.Range"].map(lambda x:int(str(x).split("-")[0]))
print loansData.head()
