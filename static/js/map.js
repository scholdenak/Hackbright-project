// Create map with location centered around specific location
function initAutocomplete() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 32.2583105, lng: -110.9144216 },
    zoom: 13,
    mapTypeId: "roadmap",
  });
  // Create the search box and link to user input element.
  const input = document.getElementById("pac-input");
  const searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  // Search within map view.
  map.addListener("bounds_changed", () => {
    searchBox.setBounds(map.getBounds());
  });
  let markers = [];
  // Add event listener to search box to retrieve new user input
  searchBox.addListener("places_changed", () => {
    const places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    // Clear out the old markers.
    markers.forEach((marker) => {
      marker.setMap(null);
    });
    markers = [];
    // For each place, get the icon, name and location.
    const bounds = new google.maps.LatLngBounds();
    places.forEach((place) => {
      if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
      }
      const icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25),
      };
      // Create a marker for each place.
      markers.push(
        new google.maps.Marker({
          map,
          icon,
          title: place.name,
          position: place.geometry.location,
        })
      );

      if (place.geometry.viewport) {
        // place markers within map viewport
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });
}

// function initMap() {
//   const map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: 32.2583105, lng: -110.9144216},
//     zoom: 12,
//     fullscreenControl: false,
//   });
//   const request = {
//     query: "Sam Hughes",
//     fields: ["name", "geometry"],
//   };
//   service = new google.maps.places.PlacesService(map);
//   service.findPlaceFromQuery(request, (results, status) => {
//     if (status === google.maps.places.PlacesServiceStatus.OK) { 
//       for (let i = 0; i < results.length; i++) {
//         createMarker(results[i]);
//       }
//       map.setCenter(results[0].geometry.location);
//     }
//   });
// }

// function createMarker(place) {
//   const marker = new google.maps.marker({
//     map,
//     position: place.geometry.location,
//   });
//   google.maps.event.addListener(marker, "click", () => {
//     infowindow.setContent(place.name);
//     infowindow.open(map);
//   });
// }

  // const input = document.getElementById("pac-input");
  // const searchBox = new google.maps.places.SearchBox(input);
  // map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

//   new google.maps.Marker({
//     position: { lat: 32.25774119157389, lng: -110.83934784940523},
//     map,
//     title: "Golf N' Stuff",
//   });
//   new google.maps.Marker({
//     position: { lat: 32.2442303786999, lng: -110.92449267017642},
//     map,
//     title: "The Loft Drive In Theater",
//   });
//   new google.maps.Marker({
//     position: { lat: 32.31246670237841,  lng: -110.82307031970466},
//     map,
//     title: "Three Canyon Beer and Wine Garden",
//   });
//   new google.maps.Marker({
//     position: { lat: 32.288516274567705, lng:-110.92263469539438},
//     map,
//     title: "Green Things Nursery",
//   });
//   new google.maps.Marker({
//     position: { lat: 32.24137471021612, lng: -110.90622631586236},
//     map,
//     title: "Black Crown Coffee Company",
//   });
//   new google.maps.Marker({
//     position: { lat: 32.253505747332056, lng: -110.89018000686586},
//     map,
//     title: "Firetruck Brewing Company",
//   });
//   new google.maps.Marker({
//     position: { lat: 32.29083694231202, lng: -110.94305229509007
//     },
//     map,
//     title: "Reforma Modern Mexican",
//   });
// }
