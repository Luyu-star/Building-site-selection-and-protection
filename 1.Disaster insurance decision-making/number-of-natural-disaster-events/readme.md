# Number of recorded natural disaster events - Data package

This data package contains the data that powers the chart ["Number of recorded natural disaster events"](https://ourworldindata.org/grapher/number-of-natural-disaster-events?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website. It was downloaded on May 16, 2025.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Disasters
Number of reported natural disasters in any given year. Note that the historical increase largely reflects improvements in data reporting, and should not be used to assess the total number of events.
Last updated: April 11, 2024  
Next update: June 2025  
Date range: 1900–2024  
Unit: events  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
EM-DAT, CRED / UCLouvain (2024) – with major processing by Our World in Data

#### Full citation
EM-DAT, CRED / UCLouvain (2024) – with major processing by Our World in Data. “Disasters – EM-DAT” [dataset]. EM-DAT, CRED / UCLouvain, “Natural disasters” [original data].
Source: EM-DAT, CRED / UCLouvain (2024) – with major processing by Our World In Data

### What you should know about this data
* EM-DAT defines a disaster as a situation or event which overwhelms local capacity, necessitating a request to the national or international level for external assistance; an unforeseen and often sudden event that causes great damage, destruction, and human suffering. Of all EM-DAT disasters, we select geophysical, meteorological, hydrological, and climatological events, which include droughts, earthquakes, extreme temperatures, floods, glacial lake outburst floods, mass movements, extreme weather events, volcanic activity, and wildfires.
* Drought is defined as an extended period of unusually low precipitation that produces a shortage of water for people, animals, and plants. Drought is different from most other hazards in that it develops slowly, sometimes even over the years, and its onset is generally difficult to detect.
* An earthquake is defined as a sudden movement of a block of the Earth's crust along a geological fault and associated ground shaking. The data includes the impacts of earthquake events, aftershocks and tsunamis.
* Extreme temperature is used as a general term for temperature variations above (extreme heat) or below (extreme cold) normal conditions.
* Extreme weather events include tornadoes, hailstorms, thunderstorms, sandstorms, blizzards, and extreme wind events.
* Flood is used as a general term for the overflow of water from a stream channel onto normally dry land in the floodplain (riverine flooding), higher-than-normal levels along the coast (coastal flooding) and in lakes or reservoirs as well as ponding of water at or near the point where the rain fell (flash floods).
* Volcanic activity is defined as any type of volcanic event near an opening/vent in the Earth's surface including volcanic eruptions of lava, ash, hot vapor, gas, and pyroclastic material.
* A wildfire is defined as any uncontrolled and non-prescribed combustion or burning of plants in a natural setting such as a forest, grassland, brush land or tundra, which consumes natural fuels and spreads based on environmental conditions (e.g., wind, or topography). Wildfires can be triggered by lightning or human actions.
* A dry mass movement is defined as any type of downslope movement of earth materials under hydrological dry conditions.
* A wet mass movement is defined as a type of mass movement that occur when heavy rain or rapid snow/ice melt send large amounts of vegetation, mud, or rock down a slope driven by gravitational forces.
* Glacial lake outburst floods are defined as those that occur when water held back by a glacier or moraine is suddenly released. Glacial lakes can be at the front of the glacier (marginal lake) or below the ice sheet (sub-glacial lake).
* Fog is defined as water droplets that are suspended in the air near the Earth's surface. Fog is simply a cloud that is in contact with the ground. Currently, the only fog disaster recorded in EM-DAT is the Great Smog of London in 1952.

### Source

#### EM-DAT, CRED / UCLouvain – Natural disasters
Retrieved on: 2024-04-11  
Retrieved from: https://emdat.be/  


    