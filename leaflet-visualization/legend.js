// Store URL in a variable 
let url = ___

// Use D3 library to access API 
d3.json(url).then(function (data) {
    console.log(data);
    newFeature(data.features);
}); 

// Set Marker size based on number of observations
function markersize(density) {
    return density * 2500;
};


// Determine color of point based on bird density/ observation count at each coord pair 
function color(bird) {
    if (bird < 250) return "#FBDD49" ;
    else if (bird < 500) return "#FF8103";
    else if (bird < 700) return "#FF1C6A";
    else if (bird < 1000) return "#E200A3";
    else if (bird < 4000) return "#9B04D";
    else return "#6D1DC6";
;


}

// Here we create a legend control object.
{var legend = L.control({
    position: "bottomleft"
});
// Then add all the details for the legend
legend.onAdd = function () {
    var div = L.DomUtil.create("div", "info legend");
    var density = [___];
    var colors = [
    "#FBDD49",
    "#FF8103",
    "#FF1C6A",
    "#E200A3",
    "#9B04DB",
    "#6D1DC6",
    ];
    div.innerHTML += "<h3 style='text-align: center'> Bird Density </h3>"
    // Looping through our intervals to generate a label with a colored square for each interval.
    for (var i = 0; i < density.length; i++) {
    div.innerHTML += "<i style='background: " + colors[i] + "'></i> "
        + density[i] + (density[i + 1] ? "&ndash;" + density[i + 1] + "<br>" : "+");
    }
return div;
};
// Finally, we our legend to the map.
legend.addTo(myMap)};