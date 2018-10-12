// Create our initial map object
// Set the longitude, latitude, and the starting zoom level
var myMap = L.map("map").setView([39.8283, -98.5795], 5);

// Add a tile layer (the background map image) to our map
// Use the addTo method to add objects to our map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: "pk.eyJ1IjoiYW5kcmV3ZGtyb2ciLCJhIjoiY2puMmgyMHV5MmtwMzNwbm81M3A5eXBhcCJ9.KzeuDq5504VtSssVial3Ow"
}).addTo(myMap);

// Create a red circle over Dallas
L.circle([32.77, -96.79], {
  color: "red",
  fillColor: "red",
  fillOpacity: 0.75,
  radius: 500
}).addTo(myMap);


// Connect a black line from NYC to Toronto


// Create a purple polygon that covers the area in Atlanta, Savannah, Jacksonville and Montgomery
