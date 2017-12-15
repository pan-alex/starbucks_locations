import pandas as pd
import math
# import matplotlib.pyplot as plt


data_starbucks = pd.read_csv('Starbucks Locations.csv')

#
# The aim of this script is to be able to work out distances between each
# Starbucks location based on their GPS coordinates.
#
# Subtraction of two coordinates should provide their Euclidean distances,
# assuming that the Earth is spherical.
#

###

class Coordinate(object):
	def __init__(self, lat, lon):
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
		d = 6371 * c    # 6371km = Earth's radius
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
