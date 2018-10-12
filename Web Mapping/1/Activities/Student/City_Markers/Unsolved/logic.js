// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Add a tile layer to the map
L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
      "access_token=pk.eyJ1IjoiYW5kcmV3ZGtyb2ciLCJhIjoiY2puMmgyMHV5MmtwMzNwbm81M3A5eXBhcCJ9.KzeuDq5504VtSssVial3Ow"
  ).addTo(myMap);

// City markers

// Add code to create a marker for each city below and add it to the map
function markerSize(population) {
  return population / 40;
}

var cities = [
  {
    name: "New York",
    location: [40.7128, -74.0059],
    population: 8550405
  },
  {
    name: "Chicago",
    location: [41.8781, -87.6298],
    population: 2720546
  },
  {
    name: "Houston",
    location: [29.7604, -95.3698],
    population: 2296224
  },
  {
    name: "Los Angeles",
    location: [34.0522, -118.2437],
    population: 3971883
  },
  {
    name: "Omaha",
    location: [41.2524, -95.9980],
    population: 446599
  }
];

// Loop through the cities array and create one marker for each city object
for (var i = 0; i < cities.length; i++) {
  L.circle(cities[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: "purple",
    // Setting our circle's radius equal to the output of our markerSize function
    // This will make our marker's size proportionate to its population
    radius: markerSize(cities[i].population)
  }).bindPopup("<h1>" + cities[i].name + "</h1> <hr> <h3>Population: " + cities[i].population + "</h3>").addTo(myMap);
}