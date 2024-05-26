from mongoengine import Document, StringField, DateTimeField, FloatField, ListField, EmbeddedDocumentField, EmbeddedDocument, ObjectIdField
from datetime import datetime

class Track(EmbeddedDocument):
  id = ObjectIdField(primary_key=True) 
  latitude = FloatField()
  longitude = FloatField()
  altitude = FloatField()
  created = DateTimeField(default=datetime.utcnow)
  meta = {
    'collection': 'tracks'  # Nombre de la colección a la que deseas mapear
  }

  @classmethod
  def from_map(cls, map):
    return cls(
      id=map.get('_id'),
      latitude=map['latitude'],
      longitude=map['longitude'],
      altitude=map['altitude'],
      created=datetime.fromisoformat(map['created']),
    )

  # Método para convertir el objeto Track a diccionario
  def to_map(self):
    map_data = {
      'latitude': self.latitude,
      'longitude': self.longitude,
      'altitude': self.altitude,
      'created': self.created.isoformat(),
    }
    if self.id:  # Agregar el campo id si está <presente en el documento
      map_data['id'] = self.id
    return map_data
