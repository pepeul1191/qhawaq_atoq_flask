from mongoengine import StringField, DateTimeField, FloatField, EmbeddedDocument, ObjectIdField
from bson import ObjectId
from datetime import datetime

class Picture(EmbeddedDocument):
  id = ObjectIdField(primary_key=True) 
  url = StringField()
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
      id=ObjectId(map.get('_id')) if map.get('_id') else None,
      url=map.get('url'),
      latitude=map['latitude'],
      longitude=map['longitude'],
      altitude=map['altitude'],
      created=datetime.fromisoformat(map['created']),
    )

  # Método para convertir el objeto Track a diccionario
  def to_map(self):
    map_data = {
      'url': self.url,
      'latitude': self.latitude,
      'longitude': self.longitude,
      'altitude': self.altitude,
      'created': self.created.isoformat(),
    }
    if self.id:  # Agregar el campo id si está <presente en el documento
      map_data['id'] = self.id
    return map_data
