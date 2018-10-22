// function buildCharts() {

//   // @TODO: Use `d3.json` to fetch the sample data for the plots
//   d3.json(`/samples`).then(function(data) {
//     // @TODO: Build a histogram
//     var x_values = data.item;

//     var trace1 = {
//       x: x_values,
//       type: 'histogram'
//       } 
//     };

//     var data = [trace1];

//     var layout = {
//       xaxis: { title: "Items"},
//     };

//     Plotly.newPlot('histogram', data, layout);
    
//   });   
// }

// buildCharts();