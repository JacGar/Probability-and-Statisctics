import pandas as pd
from scipy import stats as stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

def statistics():
    global data
    data=[i.split(',') for i in data.splitlines()]
    column_names = data[0]
    data_rows = data[1:]
    df = pd.DataFrame(data_rows, columns = column_names)
    df["Alcohol"]=df["Alcohol"].astype(float)
    df["Tobacco"]=df["Tobacco"].astype(float)

    print "Alcohol dataset stats:"
    print "Mean = ",df['Alcohol'].mean()
    print "Median =",df['Alcohol'].median()
    print "Mode =", stats.mode(df["Alcohol"])
    print "Range =",max(df['Alcohol']) - min(df['Alcohol'])
    print "Variance =",df['Alcohol'].var()
    print "Standard Deviation =",df['Alcohol'].std()
    print "\n"

    print "Tobacco dataset stats:"
    print "Mean = ",df['Tobacco'].mean()
    print "Median =",df['Tobacco'].median()
    print "Mode =",stats.mode(df["Tobacco"])[0][0]
    print "Range =",max(df['Tobacco']) - min(df['Tobacco'])
    print "Variance =",df['Tobacco'].var()
    print "Standard Deviation =",df['Tobacco'].std()



def lesson():
    global data
    data=[i.split(',') for i in data.splitlines()]
    column_names = data[0]
    data_rows = data[1:]
    df = pd.DataFrame(data_rows, columns = column_names)
    df["Alcohol"]=df["Alcohol"].astype(float)
    df["Tobacco"]=df["Tobacco"].astype(float)

    print df['Alcohol'].mean()
    print df['Alcohol'].median()
    print stats.mode(df["Alcohol"])[0][0]
    print '\n'
    print df['Tobacco'].mean()
    print df['Tobacco'].median()
    print stats.mode(df["Tobacco"])[0][0]
    print '\n'
    print max(df['Alcohol']) - min(df['Alcohol'])
    print df['Alcohol'].std()
    print df['Alcohol'].var()
    print '\n'
    print max(df['Tobacco']) - min(df['Tobacco'])
    print df['Tobacco'].std()
    print df['Tobacco'].var()
    print "\n"
    ##z-score of Utopian people
    mean = 251
    std = 20

    x = 2.3*std+mean
    print "the days corresponding to a z-score of 2.3 is",x


statistics()
