// YOUR CODE HERE
console.log(data);

var trace1 = {
    x: data.year,
    y: data.discus_throw,
    mode: "markers",
    type: "scatter",
    name: "discus",
    marker: {   
        color: "#2077b4",
        symbol: "hexagram"}
    }

var trace2 = {
    x: data.year,
    y: data.high_jump,
    mode: "lines+markers",
    type: "scatter",
    name: "discus",
    marker: {
        size: 12,   
        color: "red",
        symbol: "circle",
        line: {
            width: 3,
            color: "gray"
        }
    },
    line: {
        width: 4,
            color: 'gray'
    }
    };

var trace3 = {
    x: data.year,
    y: data.long_jump,
    mode: "markers",
    type: "scatter",
    name: "discus",
    marker: {   
        color: "#2077b4",
        symbol: "hexagram"}
    }
    
var data = [trace1, trace2, trace3]

var layout = {title:'Olympic Plot'}

Plotly.newPlot('plot', data, layout)