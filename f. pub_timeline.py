import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('doc_with_dates.csv')
data['Pub/Form Date'] = pd.to_datetime(data['Pub/Form Date'], yearfirst=True)
data['Year'] = data['Pub/Form Date'].dt.year

pubs2012 = data[data['Year'] == 2012].count()
pubs2013 = data[data['Year'] == 2013].count()
pubs2014 = data[data['Year'] == 2014].count()
pubs2015 = data[data['Year'] == 2015].count()
pubs2016 = data[data['Year'] == 2016].count()
pubs2017 = data[data['Year'] == 2017].count()
mean = np.mean([pubs2012, pubs2012, pubs2014, pubs2015, pubs2016])
days_per_pub = np.round(365/mean, decimals=1)

print('Since the Army started publishing the new doctrinal publications in 2012 it has averaged {} new publications a year.'.format(mean))
print('This is equivalent to a new doctrinal publication every {} days.'.format(days_per_pub))
