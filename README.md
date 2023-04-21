# Project #3 - Illinois Bird Migration Patterns

## Team: Autobird
### Jessica Greco, Michael O'Leary, Connor Thomas, John Leigh, Paul Brown

## Project Summary
We want to explore bird migration patterns, with a focus on endangered species in the midwest. Using publicly available data, we will create visualizations of bird populations over time.

The practical objective was to find a large dataset (730k records), convert it into a CSV, clean the data and populate a SQLite database. Then create a Flask app server to return webpage queries. Finally, creating an interactive webpage, using HTML, JavaScript, and CSS stylesheets to present the user-filtered data in a dynamic, accurate, and visually pleasing format.

This project hinges on the communication and interaction between several independent components. The applications, libraries and tools that we used include:
- Applications
  - SQLite
  - Jupyter Lab
  - Excel
  - Flask

- Libraries
  - jquery
  - Bootstrap
  - Leaflet
  - StadiaMaps
  - D3


Repo Link: https://github.com/jngreco/bird-migrations-project 

### Data Sources:
- eBird API : https://documenter.getpostman.com/view/664302/S1ENwy59#intro 
- Visualization examples : https://science.ebird.org/en/status-and-trends 
- Illinois Audubon Society : https://illinoisaudubon.org/springmigrationdashboard/ 
- Birdcast : https://dashboard.birdcast.info/region/US-IL-031 
- eBird overview page: https://science.ebird.org/en/status-and-trends
- eBird abundance animations: 
  - https://science.ebird.org/en/status-and-trends/abundance-animations 
  - https://science.ebird.org/en/status-and-trends/abundance-animations 
- eBird Trends Map: https://science.ebird.org/en/status-and-trends/trends-maps
- eBird ShorebirdViz:  https://shorebirdviz.ebird.org/species/ameavo?week=1
- Endangered Species List : https://www.audubon.org/climate/survivalbydegrees/state/us/il 


## Steps
### Finding data sources, scraping data
### Creating a Jupyter Notebook ETL to read CSV files into SQLite
To start, we created two .ipynb files to web scrape publiclly available data regarding bird migrations. The data was then merged, cleaned, and written to a CSV file: cleanbird.  The data was then read into a a SQLite database using etl_selected_columns.ipynb.

Excel File: https://drive.google.com/file/d/1D9gYqRMf75FjYv41oDJFoQ8fWJsGW2iE/view?usp=sharing 

### A Flask session was created for analysis
SQLite is being used to host the data and perform anlysis functions. bird_alchemy.py 
### Creating Flask API endpoints
Using Flask as our locally hosted database, we then created API endpoints for the future webpage to use for queries. Returned data is JSONified. We were able to connect Flask to Leaflet using Flask_CORS.
API date filter with lat/lon grouping was added.
### Creating an interacive HTML layout 
### Creating JavaScript instructions to relay dynamic data visualization
### Using D3 to retrieve data from the Flask server
### Using Plotly to visualize the retrieved data
### Creating a grayscale basemap using Leaflet
Using StadiaMap, we created a basemap and connected it to the API.
### Overlaying plotted data and metadata on basemap 
Density data was then plotted using latitude and longitude, and grouped by species. A dropdown box allows the user to select the species and a horizontal slider allows the user to select the date range from either endpoint. The webpage uses D3 to connect to Flask, which queries our SQLite database to populate the map and metadata.
### Markers and Popup Data
The legend was added to the map, using a CSS file. The marker size is based on density. Marker popups were added to include Species, Location, Date Observed, and Time Observed. 
### Debugging, Debugging, and more Debugging




## To activate the webpage, run the following in order:
- etl_all_columns.ipynb
- etl_selected_columns.ipynb
- cleanbird.csv should be in the data folder
- bird_alchemy.py
- final-index.html