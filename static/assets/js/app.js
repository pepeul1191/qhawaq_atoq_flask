
const loadTrackLayer = (map, tracks) => {
  // Crear una capa de vectores para los marcadores
  const vectorSource = new ol.source.Vector();
  const vectorLayer = new ol.layer.Vector({
    source: vectorSource
  });

  // Definir el estilo del icono
  const iconStyle = new ol.style.Style({
    image: new ol.style.Icon({
      src: BASE_URL + 'assets/img/marker.png', // Asegúrate de que esta URL sea correcta
      scale: 1.5, // Puedes ajustar el tamaño del icono según sea necesario
      anchor: [0.5, 1], // Ancla el icono en la base
      crossOrigin: 'anonymous' // Permite cargar imágenes de diferentes dominios
    })
  });

  // Añadir los marcadores al mapa
  tracks.forEach(track => {
    const feature = new ol.Feature({
      geometry: new ol.geom.Point(ol.proj.fromLonLat([track.longitude, track.latitude])), // Asegúrate de acceder correctamente a los valores de latitud y longitud
      id: track._id, // Asegúrate de acceder correctamente al ID
      created: track.created, // Asegúrate de acceder correctamente a la fecha
      altitude: track.altitude // Asegúrate de acceder correctamente a la altitud
    });
    feature.setStyle(iconStyle);
    vectorSource.addFeature(feature);
  });

  map.addLayer(vectorLayer);

  // Añadir un popup al hacer clic en un marcador
  const element = document.createElement('div');
  element.setAttribute('id', 'popup');
  element.style.position = 'absolute';
  element.style.backgroundColor = 'white';
  element.style.padding = '5px';
  element.style.border = '1px solid black';
  element.style.display = 'none';

  document.body.appendChild(element);

  const popup = new ol.Overlay({
    element: element,
    positioning: 'bottom-center',
    stopEvent: false,
    offset: [0, -10]
  });
  map.addOverlay(popup);

  map.on('click', function (event) {
    const feature = map.forEachFeatureAtPixel(event.pixel, function (feature) {
      return feature;
    });
    if (feature) {
      const coordinates = feature.getGeometry().getCoordinates();
      popup.setPosition(coordinates);
      const info = `
        <p><strong>ID:</strong> ${feature.get('id')}</p>
        <p><strong>Latitud:</strong> ${feature.getGeometry().getCoordinates()[1]}</p>
        <p><strong>Longitud:</strong> ${feature.getGeometry().getCoordinates()[0]}</p>
        <p><strong>Altitud:</strong> ${feature.get('altitude')}</p>
        <p><strong>Fecha:</strong> ${feature.get('created')}</p>
      `;
      element.innerHTML = info;
      element.style.display = 'block';
    } else {
      element.style.display = 'none';
    }
  });
}

const loadPictureLayer = (map, pictures) => {
  // Crear una capa de vectores para los marcadores
  const vectorSource = new ol.source.Vector();
  const vectorLayer = new ol.layer.Vector({
    source: vectorSource
  });

  // Definir el estilo del icono
  const iconStyle = new ol.style.Style({
    image: new ol.style.Icon({
      src: BASE_URL + 'assets/img/camera.png', // Asegúrate de que esta URL sea correcta
      scale: 1.5, // Puedes ajustar el tamaño del icono según sea necesario
      anchor: [0.5, 1], // Ancla el icono en la base
      crossOrigin: 'anonymous' // Permite cargar imágenes de diferentes dominios
    })
  });

  // Añadir los marcadores al mapa
  pictures.forEach(picture => {
    const feature = new ol.Feature({
      geometry: new ol.geom.Point(ol.proj.fromLonLat([picture.longitude, picture.latitude])), // Asegúrate de acceder correctamente a los valores de latitud y longitud
      id: picture._id, // Asegúrate de acceder correctamente al ID
      created: picture.created, // Asegúrate de acceder correctamente a la fecha
      altitude: picture.altitude,
      url: picture.url, // Asegúrate de acceder correctamente a la altitud
    });
    feature.setStyle(iconStyle);
    vectorSource.addFeature(feature);
  });

  map.addLayer(vectorLayer);

  // Añadir un popup al hacer clic en un marcador
  const element = document.createElement('div');
  element.setAttribute('id', 'popup');
  element.style.position = 'absolute';
  element.style.backgroundColor = 'white';
  element.style.padding = '5px';
  element.style.border = '1px solid black';
  element.style.display = 'none';

  document.body.appendChild(element);

  const popup = new ol.Overlay({
    element: element,
    positioning: 'bottom-center',
    stopEvent: false,
    offset: [0, -10]
  });
  map.addOverlay(popup);

  map.on('click', function (event) {
    const feature = map.forEachFeatureAtPixel(event.pixel, function (feature) {
      return feature;
    });
    if (feature) {
      const coordinates = feature.getGeometry().getCoordinates();
      popup.setPosition(coordinates);
      const info = `
        <p><strong>ID:</strong> ${feature.get('id')}</p>
        <p><strong>Latitud:</strong> ${feature.getGeometry().getCoordinates()[1]}</p>
        <p><strong>Longitud:</strong> ${feature.getGeometry().getCoordinates()[0]}</p>
        <p><strong>Altitud:</strong> ${feature.get('altitude')}</p>
        <p><strong>Fecha:</strong> ${feature.get('created')}</p>
        <strong>Imagen:</strong><img src="${BASE_URL}uploads/${feature.get('url')}" height=290 width=218/>
      `;
      element.innerHTML = info;
      element.style.display = 'block';
    } else {
      element.style.display = 'none';
    }
  });
}

const fetchData = (map) => {
  fetch(BASE_URL + 'trip/66528a136020f886d4000000')
    .then(response => {
      if (!response.ok) {
        throw new Error('Error en la solicitud: ' + response.status);
      }
      return response.json();
    })
    .then(data => {
      loadTrackLayer(map, data.tracks);
      loadPictureLayer(map, data.pictures);
    })
    .catch(error => {
      console.error('Error en la solicitud:', error);
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
  const map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-77.0157316, -12.0839347]),
      zoom: 15
    })
  });
  fetchData(map);
});
