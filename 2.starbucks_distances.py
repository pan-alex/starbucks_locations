
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

map_resolution='c'    # 'c' for development, 'f' to publish
data_starbucks = pd.read_csv('Starbucks Locations.csv')

#
# The aim of this script is to be able to work out distances between each
# Starbucks location based on their GPS coordinates.
#
# Subtraction of two coordinates should provide their Great Circle distances,
# assuming that the Earth is spherical.
#

###

class Coordinate(object):
	def __init__(self, lon, lat):
		self.lat = lat
		self.lon = lon

	def __str__(self):
		return '(' + str(self.lat) + ', ' + str(self.lon) + ')'

	def __sub__(self, other):
		# Implement Haversine Formula to calculate distance between two GPS
		# coordinates. Assumes spherical Earth. Units are in km.

		# Convert degree coordinates to radians
		deg_to_rad = math.pi / 180
		phi1 = self.lat * deg_to_rad
		phi2 = other.lat * deg_to_rad
		d_phi = (self.lat - other.lat) * deg_to_rad
		d_lambda = (self.lon - other.lon) * deg_to_rad

		# Haversine formula
		alpha = math.sin(d_phi/2)**2 \
		        + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda/2)**2
		c = 2 * math.atan2(alpha**0.5, (1 - alpha)**0.5)
		d = 6370.997 * c    # 6370.997km = Earth's radius
		return d

###

# Add a new column to the data that is a coordinate object.

# c = pd.Series
# for i in range(len(data_starbucks['Longitude']):
# 	temp = data_starbucks['Longitude'][i], data_starbucks['Latitude'][i])
#

data_starbucks['GPS'] = \
	data_starbucks.apply(lambda row:
                         Coordinate(row['Longitude'], row['Latitude']),
                         axis = 'columns'
                         )


# Examples of stupid stuff you can do:

# How many stores are within __km of my house?
km = 10
my_house = Coordinate(-79.40, 43.66)

data_starbucks['dist'] = data_starbucks.apply(
	lambda row: my_house - row['GPS'],
	axis = 'columns')

print(data_starbucks[data_starbucks['dist'] <= km])

# Which store is nearest to my house?
closest = data_starbucks.sort_values('dist').head(1)

#           Brand Store Number                      Store Name Ownership Type  \
# 1719  Starbucks   72457-7627  U of Toronto - Robarts Library       Licensed
#      Street Address     City State/Province Country Postcode  Phone Number  \
# 1719  369 Huron St.  Toronto             ON      CA  M5S 1A5  416-591-1647
#                        Timezone  Longitude  Latitude             GPS      dist
# 1719  GMT-05:00 America/Toronto      -79.4     43.66  (43.66, -79.4)  0.540616

# Which store is the furthest away from my house?
furthest = data_starbucks.sort_values('dist', ascending=False).head(1)

#          Brand  Store Number          Store Name Ownership Type  \
# 290  Starbucks  25286-240412  DFO Spencer Street       Licensed
#                            Street Address       City State/Province Country  \
# 290  93-161 Spencer Street, 201, 202, 203  Melbourne            VIC      AU
#     Postcode Phone Number                       Timezone  Longitude  Latitude  \
# 290     3000          NaN  GMT+10:00 Australia/Melbourne     144.95    -37.82
#                   GPS         dist
# 290  (-37.82, 144.95)  16268.21892

# I will have to visit.

#
#
#
#
#

# World Map with Starbucks Locations
plt.clf()
m = Basemap(projection='merc',llcrnrlat=-60,urcrnrlat=84,\
            llcrnrlon=-180,urcrnrlon=180,resolution=map_resolution)
m.drawmapboundary(fill_color='deepskyblue')
m.fillcontinents(color='white',lake_color='deepskyblue')
# m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
# m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1]
lat, lon = m(np.array(data_starbucks['Longitude']),
             np.array(data_starbucks['Latitude']))
m.plot(lat, lon, 'o', color='k', markersize='1', alpha = 0.25)
plt.title("Starbucks Locations Around The World")

# m.drawcoastlines(color='white')

# Some more useless stuff you can do:

# Draw a great circle line fom my nearest Starbucks location to my furthest:
lon1, lat1 = float(closest['Longitude']), float(closest['Latitude'])
lon2, lat2 = float(furthest['Longitude']), float(furthest['Latitude'])

m.drawgreatcircle(lon1, lat1, lon2, lat2, alpha = 0.5)