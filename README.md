# Spring vs Fall Thunderstorm Wind Events in Texas (1955–2025)

The purpose of this module will be to compare the number of severe weather events in Texas between meterological fall and spring.
The data set in this module is using "Thunderstorm Wind" events from the Storm Events Database, https://www.ncei.noaa.gov/stormevents.

The real purpose of this module is to see if there is an increase in severe storms in these seasons over the past 70 years, as especially recently we have had very active fall severe seasons so I wanted to see if there was truth behind that thought. 
Using "Thunderstorm Wind" events was more by how the ncei site allows you to download this data and from the filters that were avalible, thunderstorm wind allowed the broadest bearth of severe events that it could be used to get a simple numbers advandtage to get a decent ammount of data as you can see by some of the earlier decades, the data is sparse.


- NOAA/NCEI Storm Events Database: NOAA National Centers for Environmental Information (NCEI). Storm Events Database. Accessed Dec 2025. DOI: 10.7289/V5KW5D8S.
- U.S. Census Bureau, Cartographic Boundary Files, Counties, 2018 (5m). Accessed Dec 2025.

# Spring vs Fall Thunderstorm Wind Events in Texas (1955–2025)
-Motivation
Thunderstorm wind events are a major hazard in Texas, causing damage to property and risks to public safety. In recent years, fall severe weather seasons have seemed unusually active. This project asks a simple question:
Are fall thunderstorm wind events increasing relative to spring over the past 70 years?
Approach
• 	Dataset: NOAA/NCEI Storm Events Database, filtered for Texas and “Thunderstorm Wind” events.
• 	Timeframe: 1955–2025.
• 	Processing: Dates are parsed and events are classified into meteorological spring (March–May) and fall (September–November). Coordinates are cleaned and mapped to Texas counties.
• 	Analysis:
• 	Yearly counts by season.
• 	Interactive maps with county boundaries, season toggles, and year slider.
• 	Statistical tests (chi‑square) and regression slopes to measure differences and long‑term trends.
Results
• 	Spring historically has more thunderstorm wind events, but fall shows notable increases in recent decades.
• 	Chi‑square testing confirms that seasonal distributions differ significantly across the 1955–2025 record.
• 	Regression slopes suggest fall events are increasing faster than spring.
• 	Interactive maps highlight regional clustering and changes across decades.
Conclusions
• 	Seasonal risk profiles in Texas are shifting, with fall severe weather becoming more prominent.
• 	While reporting practices have changed over time, the long‑term trend points to a real increase in fall events.
• 	These findings suggest that fall severe weather deserves greater attention in forecasting, planning, and public communication.
Reproducibility
• 	Environment: See  for dependencies.
• 	Code: Core functions are in .
• 	Notebook:  contains motivation, approach, results, and conclusions.
• 	Data: Raw CSVs are not committed; download instructions are provided in .
Citations
• 	NOAA National Centers for Environmental Information (NCEI). Storm Events Database. Accessed Dec 2025. DOI: 10.7289/V5KW5D8S.
• 	U.S. Census Bureau. Cartographic Boundary Files, Counties, 2018 (5m). Accessed Dec 2025.