    
// https://bl.ocks.org/d3noob/6f082f0e3b820b6bf68b78f2f7786084

var vmax = 640;
var hmax = 480;

// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = vmax - margin.left - margin.right,
    height = hmax - margin.top - margin.bottom;

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("figure").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
        .attr("viewBox", "0 0 "+vmax+" "+hmax); /// Dynamically resizes the svg image
// .attr("class", "img-fluid")        /// Dynamically resizes the svg image.
// .attr("width", "100%")             /// Dynamically resizes the svg image.

// set the ranges
var x = d3.scaleLinear()
        .range([0, width]);
var y = d3.scaleLinear()
        .range([height, 0]);

var xaxis =d3.axisBottom(x)
        .scale(x);
var yaxis =d3.axisLeft(y)
        .scale(y);

    // Add the X Axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xaxis);

// Add the Y Axis
svg.append("g")
    .attr("class", "y axis")
    .call(yaxis);

// Add a box for scatter data
var databox = svg.append("g")
        .attr("class","datapoints");

function scatter(data){    
    
    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.x; }));
    y.domain([0, d3.max(data, function(d) { return d.y; })]);
            
    // // define the line
    // var valueline = d3.line()
    //     .x(function(d) { return x(d.x); })
    //     .y(function(d) { return y(d.y); });

    // // Add the valueline path.
    // svg.append("path")
    // .data([data])
    // .attr("class", "line")
    // .attr("d", valueline);

    // Add the scatterplot
    var scat = databox.selectAll("circle")
            .data(data);

    scat.exit()
        .remove();

    scat.enter()
        .append("circle")
        .attr("r", 5)
        .attr("cx", function(d) { return x(d.x); })
        .attr("cy", function(d) { return y(d.y); });

    scat
        .attr("cx", function(d) { return x(d.x); })
        .attr("cy", function(d) { return y(d.y); });

    svg.selectAll(".x")
        .transition()
            .call(xaxis);

    svg.selectAll(".y")
        .transition()
        .call(yaxis);

    
    // });

}
