function init() {
  var data = [{
    values: [19, 26, 55, 88],
    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  var plot = document.getElementById("pie");

  // Note the extra brackets around 'newx' and 'newy'
  Plotly.restyle(plot, "values", [newdata]);
}

function getData(dataset) {
  // YOUR CODE HERE
  // create a select statement to select different data arrays (YOUR CHOICE)
  // whenever the dataset parameter changes. This function will get called
  // from the dropdown event handler.

  var labels = ["d","r","o","p"];
  var data = [];

  switch(dataset){
    case "iTunes":
      data = [10, 25, 39];
      break;
    case "Spotify":
      data = [10, 5, 9];
      break;
    case "Pandora":
      data = [1, 45, 39];
      break;
    case "Soundcloud":
      data = [1, 4, 3];
      break;
  }


  updatePlotly(data);
}

init();
