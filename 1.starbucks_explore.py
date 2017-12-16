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
data_starbucks['Country'].value_counts()[:25]    # Top 3: US, China, Canada

data_starbucks['Country'].value_counts()[:25].plot('bar')
plt.show()


# Which cities have the most Starbucks?

data_starbucks['City'].value_counts()[:25]

# Toronto has a lot of Starbucks.
# 上海市 (#1) is Shanghai, 北京市 (#3) is Beijing
# 서울 (#14) is Seoul, which actually appears as 'Seoul' in position #2
# 杭州市 (#22) is Hangzhou, 深圳市 (#23) is Shenzhen, 广州市 (#25) is Guangzhou.

# Some of these cities have English names listed here as well.
# Change these names to English:
city_names = {'上海市': 'Shanghai',
              '北京市': 'Beijing',
              '서울': 'Seoul',
              '杭州市': 'Hangzhou',
             '深圳市': 'Shenzhen',
             '广州市': 'Guangzhou'}

data_starbucks = data_starbucks.replace({'City': city_names})
cities_starbucks = data_starbucks['City'].value_counts()

cities_starbucks[:25].plot('bar', width = 0.9)
plt.title('Cities with the most Starbucks Locations')
plt.ylabel('Number of Starbucks stores')
plt.tight_layout()
plt.show()


# Which city has the highest Starbucks to people ratio?

# Load in Population data:
# Data from https://nordpil.com/resources/world-database-of-large-cities/
# Which I believe uses data from the UN
data_populations = pd.read_csv("World City Populations.csv",
                               encoding='latin1')

# *** DISCLAIMER: The UN data aggregate municipalities into large urban areas,
# whereas the Starbucks data list their store locations by municipality (i.e.,
# the number of Starbucks locations per urban area are underestimated). Example:
# Mississauga and Hamilton fall under the 'Toronto' urban area in the UN data,
# but are listed separately in the Starbucks data. ***


# Data are a bit dirty, so some clean up:
mask_nulls = data_populations['City'].isnull()
data_populations.loc[mask_nulls, 'City'] = data_populations.loc[mask_nulls, 'ID']

data_populations = data_populations.set_index('City')
###################

# Number of stores / population of the city
density_starbucks = cities_starbucks / \
                    data_populations.loc[cities_starbucks.keys()]['pop2015']

# Some cities not included in population data, or have incompatible characters
density_starbucks = density_starbucks[density_starbucks.notnull()]

# Population data are in 1000s, multiply by 100 to express as stores per 100,000
density_starbucks = density_starbucks * 100

density_starbucks.sort_values(ascending = False)[:25].plot('bar', width=0.9)
plt.title('Hippest Places on Earth: Cities with the highest density ' +
          'of Starbucks Stores (2015 population)')
plt.ylabel('Number of Starbucks stores per 100,000 people')
plt.tight_layout()
plt.show()


#############

# #
# # Now looking at Canadian Stores Only.
# #
#
# data_canada = data_starbucks[data_starbucks['Country'] =='CA']
#
#
# data_canada.head()
#
#
# # Starbucks Locations by Province
# data_canada['State/Province'].value_counts()
# data_canada['State/Province'].value_counts().plot('bar')
# plt.show()
#
#
#
#
# data_canada['Latitude'].max()
# data_canada['Latitude'].min()
# data_canada['Latitude'].median()
# # Our Starbucks stores call between 42.25 and 60.7 longitude. Median = 49.


