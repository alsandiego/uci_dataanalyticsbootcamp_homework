// from data.js
var tableData = data;

// print data from data.js
console.log(data)

// YOUR CODE HERE!
// Get a reference to the table body
var tbody = d3.select("tbody");
// Select the button
var button = d3.select("#filter-btn");

// Appends data to table in index.html
data.forEach((ufoSighting) => {
  var row = tbody.append("tr");
  Object.entries(ufoSighting).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

// Filter data when Button is pressed

// Complete the click handler for the form
button.on("click", function() {

    // Select the input element and get the raw HTML node
    var inputElement = d3.select('#datetime')
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    console.log(inputValue)
    // Use the form input to filter the data by blood type
    var matchedSighting = tableData.filter(sighting => sighting.datetime === inputValue)
    console.log(matchedSighting)
  
    // clear tbody to show only matched sightings
    tbody.html("");

    // shows only matched sightings data
    matchedSighting.forEach((ufoSighting) => {
        var row = tbody.append("tr");
        Object.entries(ufoSighting).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });
  });