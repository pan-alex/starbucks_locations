library(tidyverse)
library(ggmap)

getwd()

data_starbucks <- read.csv('Python/starbucks_locations/Starbucks Locations.csv')

tapply(data_starbucks[, 'Country'])

plot(table(data_starbucks[, 'Country'])

####

data_Canada <- filter(data_starbucks, Country == 'CA')

# Number stores per province / territory
table <- table(data_Canada$State.Province)
table[table > 0]


# Map of Starbucks locations in Canada
sbuxMap <- function(location="Toronto", zoom=3, alpha=0.05, col='red') {
    myLocation = location
    myMap = get_map(location=myLocation,
                 source='google',
                 maptype='roadmap',
                 zoom=zoom,
                 crop=FALSE)
    
    ggmap(myMap) + 
        geom_point(data=data_Canada, 
                   aes(x= Longitude, y=Latitude),
                   alpha = alpha,
                   col = col)
}

# Canada
sbuxMap('Canada')


# Toronto -- We can tell from this map (and those at higher zooms) that the
# resolution on the GPS coordinates is not high enough to locate each building
# with precision.
sbuxMap('Toronto', zoom=10, alpha = 0.2)
