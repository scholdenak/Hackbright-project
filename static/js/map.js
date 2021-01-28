// let map;
// let service;
// let infowindow;

// const keyWordForm = document.querySelector("#test");

// keyWordForm.addEventListener('submit', (evt) => {
//   const keyWordInput = document.querySelector('input[id=keyword]')
// })

function initMap() {
  let map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 32.2583105, lng: -110.9144216},
    zoom: 12,
    fullscreenControl: false,
  });

  const input = document.getElementById("pac-input");
  const searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

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
}
