// from data.js
var tableData = data;

// print data from data.js on console
console.log(data)

// Get a reference to the table body and the filter button
var tbody = d3.select("tbody");
var button = d3.select("#filter-btn");

// Appends data to table in index.html when website loads
data.forEach((ufoSighting) => {
  var row = tbody.append("tr");
  Object.entries(ufoSighting).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

// Filter data when Button is pressed
button.on("click", function() {

    // Select the input element
    var inputElement = d3.select('#datetime')
  
    // Get the value property of the input element and print on console
    var inputValue = inputElement.property("value");
    console.log(inputValue)
    // Use the form input to filter the data by date and print on console
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