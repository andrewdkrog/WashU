// Create map
var mapper = L.map("map", {
    center: [40.7128, -74.0059],
    zoom: 11
});

// Send API request
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
}).addTo(mapper);

var link = "http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/" +
"35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson";

function colorPicker(borough){

    switch(borough){
        case "Brooklyn":
        return "brown";
        break;
        case "Bronx":
        return "black";
        break;
        case "Queens":
        return "blue";
        break;
        case "Manhattan":
        return "green";
        break;
        case "Staten Island":
        return "red";
        break;
        default:
        return "black";
        break;
    }
}

d3.json(link, function(dataset){
    L.geoJson(dataset, {
        style: function(feature){
            return{
                color: "white",
                fillColor: colorPicker(feature.properties.borough),
                fillOpactiy: .99,
                weight: 1.5
            }
        }
    }).addTo(mapper);
});