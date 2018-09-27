// @TODO: Complete the following sections

console.log(data.greekSearchResults);

// Sort the data array using the greekSearchResults value
data = data.sort(function(a, b){
    return parseFloat(b.greekSearchResults) - parseFloat(a.greekSearchResults)});
console.log(data);
data = data.reverse;

// Slice the first 10 objects for plotting
data = data.greekSearchResults.slice(0,10);
console.log(data);

// // Trace1 for the Greek Data
var trace1 = {
    x: data.map(row => row.greekSearchResults),
    y: data.map(row => row.greekName),
    type: 'bar',
    orientation: 'h'
};

// // set up the data variable
data = [trace1];

// // set up the layout variable
layout = {'title': 'Greek Gods'};

// // Render the plot to the div tag with id "plot"
Plotly.newPlot('plot', trace1);