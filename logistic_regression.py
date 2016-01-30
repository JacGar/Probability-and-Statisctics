import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('loansData_clean.csv')
loansData["IR_TF"]=loansData["Interest.Rate"].map(lambda x: True if x >= 0.12 else False)
print loansData[loansData['Interest.Rate'] == 0.13].head()
