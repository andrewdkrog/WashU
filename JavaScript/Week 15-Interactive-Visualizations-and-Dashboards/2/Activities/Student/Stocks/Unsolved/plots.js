var apiKey = "ie4sM5G__EeDg6Sg5wi7";

/* global Plotly */
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} data
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
function unpack(data, index) {
  return data.map(row => row[index])
}

/**
 * Fetch data and build the timeseries plot
 */
function buildPlot() {
  d3.json(url).then(function(data) {
    let date = data.dataset.data[0];
  }

trace = {
  x: dates,
  y: closingPrice
};
}

buildPlot();
