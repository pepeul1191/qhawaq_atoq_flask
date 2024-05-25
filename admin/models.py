from mongoengine import Document, StringField, DateTimeField, FloatField, ListField, EmbeddedDocumentField, EmbeddedDocument
from datetime import datetime

class Member(Document):
  id = StringField(primary_key=True) 
  names = StringField()
  last_names = StringField()
  resume = StringField()
  image_url = StringField()
  meta = {
    'collection': 'members'  # Nombre de la colección a la que deseas mapear
  }

class Picture(EmbeddedDocument):
  url = StringField()
  meta = {
    'collection': 'pictures'  # Nombre de la colección a la que deseas mapear
  }

class Track(EmbeddedDocument):
  id = StringField(primary_key=True) 
  latitude = FloatField()
  longitude = FloatField()
  altitude = FloatField()
  created = DateTimeField(default=datetime.utcnow)
  picture = EmbeddedDocumentField(Picture, null=True, required=False)
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
      picture=Picture(url=map['picture']['url']) if map.get('picture') else None
    )

  # Método para convertir el objeto Track a diccionario
  def to_map(self):
    map_data = {
      'latitude': self.latitude,
      'longitude': self.longitude,
      'altitude': self.altitude,
      'created': self.created.isoformat(),
      'picture': {'url': self.picture.url} if self.picture else None
    }
    if self.id:  # Agregar el campo id si está <presente en el documento
      map_data['id'] = self.id
    return map_data

class Trip(Document):
  id = StringField(primary_key=True) 
  created = DateTimeField()
  name = StringField()
  tracks = ListField(EmbeddedDocumentField(Track))
  meta = {
    'collection': 'trips'  # Nombre de la colección a la que deseas mapear
  }
  @classmethod
  def from_map(cls, map):
    return cls(
      id=map.get('_id'),
      created=datetime.fromisoformat(map['created']),
      name=map['name'],
      tracks=[Track.from_map(track_map) for track_map in map.get('tracks', [])]
    )

  def to_map(self):
    map_data = {
      'created': self.created.isoformat(),
      'name': self.name,
      'tracks': [track.to_map() for track in self.tracks]
    }
    if self.id:  # Agregar el campo id si está presente en el documento
      map_data['id'] = self.id
    return map_data