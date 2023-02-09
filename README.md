# weed-maps-scraper

Capable of pulling specific data from WeedMaps listing API and placing them in a .csv file.

You need to provide the URLs yourself and place them into the file, which can be obtained by navigating to:

https://weedmaps.com/dispensaries/in/united-states > select a state > select a city > inspect element > navigate to the network tab > refresh page > search for a shown dispensary name > open that listing API url > add that URL to the urls list.

Originally I had it import the URLs from a .txt file but found it easier to do it manually.

It is possible to change which data you'd like the program to pull. Currently it will pull the name, state, city, and email of the dispensary. Different headers can be found on the API URL.
