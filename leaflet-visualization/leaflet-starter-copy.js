// Set Up Variables 
var birdMap 
let base_url = 'http://127.0.0.1:5000/api/v1.0/obs_by_name_and_date/'
let dates_url = '/2023-01-01/2023-03-31'
let bird_url = 'Bald Eagle'
let full_url = base_url + bird_url + dates_url

d3.json(full_url).then(function(response) {
  console.log(response);
  //create a new marker cluster group
  var markers = L.markerClusterGroup({
    iconCreateFunction: function(cluster) {
      var childCount = cluster.getChildCount();
      var clusterClass = 'marker-cluster-small';
      if (childCount > 50) {
        clusterClass = 'marker-cluster-medium';
      }
      if (childCount > 150) {
        clusterClass = 'marker-cluster-large';
      }
      if (childCount > 300) {
        clusterClass = 'marker-cluster-xlarge';
      }
      if (childCount > 500) {
        clusterClass = 'marker-cluster-xxlarge';
      }
      if (childCount > 900) {
        clusterClass = 'marker-cluster-xxxlarge';
      }
      return L.divIcon({
        html: '<div><span>' + childCount + '</span></div>',
        className: 'marker-cluster ' + clusterClass,
        iconSize: new L.Point(40, 40),
        iconAnchor: new L.Point(20, 20),
        style: 'background-color: #FF7308; border-radius: 50%; text-align: center; font-weight: bold; font-size: 16px;'
      });
    }
  });
  console.log(markers);
  //loop through the data
  for (var i = 0; i<response.length; i++){
    //set the data location propert to a variable
    var location = response[i];
    
    if (location){
      //console.log(location);
      //add marker to the new cluster group, and bind a popup
      
      markers.addLayer(L.marker([location.LATITUDE, location.LONGITUDE])
      .bindPopup(location['COMMON_NAME'] + '<br/>' + location.LATITUDE + ', ' + location.LONGITUDE));
    }

    }
    map.addLayer(markers);

    
});