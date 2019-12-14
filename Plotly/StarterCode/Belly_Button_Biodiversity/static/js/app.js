function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  var url = `/metadata/${sample}`;
  d3.json(url).then(function(response){
    // Use d3 to select the panel with id of `#sample-metadata`
    var sample_meta = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
    sample_meta.html("");
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(response).forEach(([key, value]) => {
      sample_meta.append("p").text(`${key}: ${value}`);
    });
    console.log(sample_meta)
  });
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
};

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var samples_url =  `/samples/${sample}`;
  d3.json(samples_url).then(function(data){

    var otu_ids = data.otu_ids;
    var sample_values = data.sample_values;
    var otu_labels = data.otu_labels;

    // @TODO: Build a Bubble Chart using the sample data
    var trace1 = {
      x: otu_ids,
      y: sample_values,
      text: otu_labels,
      mode: 'markers',
      marker: {
      size: sample_values,
      color: otu_ids
      }
    };
    
    var data_bubble = [trace1];
    
    var layout = {
      xaxis: { title: 'OTU ID'}
    };
    
    bubble = document.getElementById("bubble");
    Plotly.newPlot(bubble, data_bubble, layout);

    
    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).

    // Get top 10
    var dict = [];
    for (var c = 0; c < data.otu_ids.length; c++) {
      dict.push({
          "otu_id": data.otu_ids[c],
          "sample_value": data.sample_values[c],
          "otu_label": data.otu_labels[c]
      });
    }
    dict.sort(function(a, b) {
      return parseFloat(b.sample_values) - parseFloat(a.sample_values);
    });
    dict = dict.slice(0, 10);

    var data_pie = [{
      type: "pie",
      values: dict.map(row => row.sample_value),
      labels: dict.map(row => row.otu_id),
      textinfo: "label+percent",
      textposition: "inside",
      automargin: true
    }]
    
    var layout_pie = {
      height: 500,
      width: 500,
      showlegend: true
      }

    pie = document.getElementById("pie");
    Plotly.newPlot(pie, data_pie, layout_pie);
  });

};

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();