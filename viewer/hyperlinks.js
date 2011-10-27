window.onload = (function () {
    var latlngSV = new google.maps.LatLng(0,0),
        latlng = new google.maps.LatLng(lat, lng);

    var mapOptions = {
        center: latlng,
        zoom: 14,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

    var sv = new google.maps.StreetViewService();
    sv.getPanoramaByLocation(latlng, 50, processSVData);
    var heading = google.maps.geometry.spherical.computeHeading(latlngSV, latlng);

    var panorama = new google.maps.StreetViewPanorama(document.getElementById("pano"), {
        position: latlng,
        pov: {
            heading: heading,
            pitch: 10,
            zoom: 0
        }
    });

    map.setStreetView(panorama);

    function processSVData(data, status) {
        if (status == google.maps.StreetViewStatus.OK) {
            latlngSV = data.location.latLng;
        } else {
            alert("Street View data not found for this location.");
        }
    }
});
