// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Step 3:
// Import data from the donuts.csv file
// =================================
d3.csv("assets/data/data.csv").then(function(d3Data) {
    // Step 4: Parse the data

    // Format the data
    d3Data.forEach(function(data) {
      data.healthcare = +data.healthcare;
      data.poverty = +data.poverty;
      data.abbr = +data.abbr;
    });
  
    // Step 5: Create the scales for the chart
    // =================================
    var xLinearScale  = d3.scaleLinear().range([0,height]);
  
    var yLinearScale = d3.scaleLinear().range([height, 0]);
  
    // Step 6: Set up the y-axis domain
    // ==============================================
    // @NEW! determine the max y value
    var healthcareMax = d3.max(d3Data, d => d.healthcare);
  
    var povertyMax = d3.max(d3Data, d => d.poverty);
  
    // Use the yMax value to set the yLinearScale domain
    yLinearScale.domain([4, healthcareMax]);
    xLinearScale.domain([8, povertyMax]);
  
  
    // Step 7: Create the axes
    // =================================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);
  
    // Step 8: Append the axes to the chartGroup
    // ==============================================
    // Add x-axis
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .text("In Poverty (%)")
      .call(bottomAxis);
  
    // Add y-axis
    chartGroup.append("g")
        .text("Lacks of Healthcare(%)")
        .call(leftAxis);

  
    // Step 9: append circles
    var circlesGroup = chartGroup.selectAll("circle")
    .data(d3Data)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "10")
    .attr("fill", "gold")
    .attr("stroke-width", "1")
    .attr("stroke", "black");
  
  
  }).catch(function(error) {
    console.log(error);
  });
  