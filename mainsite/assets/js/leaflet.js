var map = L.map('map').setView([37.76094, -122.41538], 14);

L.tileLayer('http://a.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
	maxZoom: 18
}).addTo(map)

map.on('click', function(e){
	console.log(e.latlng);
	$("#id_latitude").val(e.latlng.lat);
	$("#id_longitude").val(e.latlng.lng);
	L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
});
