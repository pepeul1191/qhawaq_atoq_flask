document.addEventListener('DOMContentLoaded', (event) => {
  // Coloca aquí tu código JavaScript para configurar el mapa y los marcadores

  // Datos de ejemplo (esto debería ser generado dinámicamente)
  const pictures = [
    {
      id: '665289ff6020eb86d4000000',
      url: '/assets/img/demo.png',
      latitude: -12.0839347,
      longitude: -77.0157316,
      altitude: 173.39999389648438,
      created: '2024-05-25T20:01:51.005+00:00'
    },
    {
      id: '665289ff6020eb86d4000001',
      url: '/assets/img/demo.png',
      latitude: -12.0840000,
      longitude: -77.0160000,
      altitude: 180.39999389648438,
      created: '2024-05-26T20:01:51.005+00:00'
    }
    // Agrega más objetos Picture aquí
  ];
  
  // Crear el mapa
  const map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-77.0157316, -12.0839347]), // Centrar el mapa en una ubicación inicial
      zoom: 15
    })
  });

  // Crear una capa de vectores para los marcadores
  const vectorSource = new ol.source.Vector();
  const vectorLayer = new ol.layer.Vector({
    source: vectorSource
  });

  // Añadir los marcadores al mapa
  pictures.forEach(picture => {
    const feature = new ol.Feature({
      geometry: new ol.geom.Point(ol.proj.fromLonLat([picture.longitude, picture.latitude])),
      name: picture.url,
      id: picture.id,
      created: picture.created,
      altitude: picture.altitude
    });

    // Añadir el feature a la fuente vectorial
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
        <p><strong>URL:</strong> ${feature.get('name')}</p>
        <p><strong>Latitud:</strong> ${feature.get('latitude')}</p>
        <p><strong>Longitud:</strong> ${feature.get('longitude')}</p>
        <p><strong>Altitud:</strong> ${feature.get('altitude')}</p>
        <p><strong>Fecha:</strong> ${feature.get('created')}</p>
      `;
      element.innerHTML = info;
      element.style.display = 'block';
    } else {
      element.style.display = 'none';
    }
  });
});