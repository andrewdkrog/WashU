var arr = [50, 55, 53];

// var list = d3.select("ul").selectAll("li")
// console.log("list", list);

// var list = d3.select("ul").selectAll("li").data()
// console.log("list", list);

var list = d3.select("ul").selectAll("li").data(arr)
console.log("list", list);