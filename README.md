# weed-maps-scraper

Capable of pulling specific data from WeedMaps listing API and placing them in a .csv file.

You need to provide the URLs yourself and place them into the file, which can be obtained by navigating to:

https://weedmaps.com/dispensaries/in/united-states > select a state > select a city > inspect element > navigate to the network tab > refresh page > search for a shown dispensary name > open that listing API url > add that URL to the urls list.

It is possible to have the program work by giving it a geolocation but, besides it requiring an extra 300+ lines of code (whereas this is only 30) - it wasn't too feasible for my needs.

It is possible to change which data you'd like the program to pull. Currently it will pull the name, state, city, and email of the dispensary. Different headers can be found on the API URL.

It will paginate up to 7 pages. You can change this if you'd like but from my testing, 7 is the sweet spot.
