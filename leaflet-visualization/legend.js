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