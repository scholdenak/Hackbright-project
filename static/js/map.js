let map;
// let service;
// let infowindow;

// const keyWordForm = document.querySelector('form');

// keyWordForm.addEventListener('submit', (evt) => {
//   const keyWordInput = document.querySelector('input[name=keyword]')
// })

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 32.2226, lng: -110.9747 },
    zoom: 8,
  });
  new google.maps.Marker({
    position: { lat: 32.2225, lng: -110.9748 },
    map,
    title: "It worked!",
  });
}

// function initMap() {
//   let tucson = new google.maps.LatLng(32.2226, -110.9747);
// //   infowindow = new google.maps.InfoWindow();
//   map = new google.maps.Map(document.getElementById("map"), {
//     center: tucson,
//     zoom: 13,
//   });
// }
//   let request = {
//     query: keyWordInput, //need user input
//     fields: ["name", "geometry"],
//   };
  // service = new google.maps.places.PlacesService(map);
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
//   const marker = new google.maps.Marker({
//     map,
//     position: place.geometry.location,
//   });
//   google.maps.event.addListener(marker, "click", () => {
//     infowindow.setContent(place.name);
//     infowindow.open(map);
//   });
// }

// function initAutocomplete() {
//   const map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: 32.2226, lng: -110.9747 },
//     zoom: 13,
//     mapTypeId: "roadmap",
//   });
//   // Create the search box and link it to the UI element.
//   const input = document.getElementById("pac-input");
//   const searchBox = new google.maps.places.SearchBox(input);
//   map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
//   // Bias the SearchBox results towards current map's viewport.
//   map.addListener("bounds_changed", () => {
//     searchBox.setBounds(map.getBounds());
//   });
//   let markers = [];
//   // Listen for the event fired when the user selects a prediction and retrieve
//   // more details for that place.
//   searchBox.addListener("places_changed", () => {
//     const places = searchBox.getPlaces();

//     if (places.length == 0) {
//       return;
//     }
//     // Clear out the old markers.
//     markers.forEach((marker) => {
//       marker.setMap(null);
//     });
//     markers = [];
//     // For each place, get the icon, name and location.
//     const bounds = new google.maps.LatLngBounds();
//     places.forEach((place) => {
//       if (!place.geometry) {
//         console.log("Returned place contains no geometry");
//         return;
//       }
//       const icon = {
//         url: place.icon,
//         size: new google.maps.Size(71, 71),
//         origin: new google.maps.Point(0, 0),
//         anchor: new google.maps.Point(17, 34),
//         scaledSize: new google.maps.Size(25, 25),
//       };
//       // Create a marker for each place.
//       markers.push(
//         new google.maps.Marker({
//           map,
//           icon,
//           title: place.name,
//           position: place.geometry.location,
//         })
//       );

//       if (place.geometry.viewport) {
//         // Only geocodes have viewport.
//         bounds.union(place.geometry.viewport);
//       } else {
//         bounds.extend(place.geometry.location);
//       }
//     });
//     map.fitBounds(bounds);
//   });
// }