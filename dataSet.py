import numpy as np
import plotly_express as px
import csv
def getDataSource(dataPath):
    iceCreamSales=[]
    coldDrinkSales=[]
    with open(dataPath) as f:
        df=csv.DictReader(f)
        for row in df:
            iceCreamSales.append(float(row['Temperature']))
            coldDrinkSales.append(float(row['Ice-cream Sales']))
    return{'x':iceCreamSales,'y':coldDrinkSales}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('the correlation between temperature and ice cream sales is : \n', correlation[0,1])
def setUp():
    dataPath='Ice-Cream.csv'
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
setUp()