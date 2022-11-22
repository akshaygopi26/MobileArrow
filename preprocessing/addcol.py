import pandas as pd  
import math
import numpy as np
data = pd.read_csv('flipkart.csv')
data1=data[['sales_price','sales']]
data1.sales=data1.sales*10000000
units_sold = data1.sales/data1.sales_price
data['units_sold']=units_sold.apply(np.floor).astype(int)
data.to_csv('flipkart2.csv')
