# This is a simple data exploration of the Starbucks Locations data set.
#
#
#
#
#

import pandas as pd
import matplotlib.pyplot as plt


data_starbucks = pd.read_csv('Starbucks Locations.csv')


data_starbucks.shape    # 13 variables on 25600 stores
data_starbucks.head()

# How many NaNs in each column?
data_starbucks.isnull().sum()    # Data are pretty clean for the most part.

# Number of stores per country?
data_starbucks['Country'].value_counts()    # Top 3: US, China, Canada

data_starbucks['Country'].value_counts().plot('bar')
plt.show()


#############

#
# Now looking at Canadian Stores Only.
#

data_canada = data_starbucks[data_starbucks['Country'] =='CA']


data_canada.head()


# Starbucks Locations by Province
data_canada['State/Province'].value_counts()
data_canada['State/Province'].value_counts().plot('bar')
plt.show()




data_canada['Latitude'].max()
data_canada['Latitude'].min()
data_canada['Latitude'].median()
# Our Starbucks stores call between 42.25 and 60.7 longitude. Median = 49.


