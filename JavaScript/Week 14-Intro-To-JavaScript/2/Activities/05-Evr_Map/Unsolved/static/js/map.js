// The Stages of JavaScript
var theStagesOfJS = ["confidence", "sadness", "confusion", "realization", "debugging", "satisfaction"];

// Challenge Activity
var princesses = [
  { name: "Rapunzel", age: 18 },
  { name: "Mulan", age: 16 },
  { name: "Anna", age: 18 },
  { name: "Moana", age: 16 }
];

// Log the name of each princess, follow by a colon, followed by their age
// Hint: use forEach
princesses.forEach(function(princesses) {
  console.log(princesses.name,": ", princesses.age);
});

// Create an array of just the names from the princesses array
// Hint: use map
var names = princesses.map(function(princesses){
  return princesses.name;
})

console.log(names)