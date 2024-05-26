from mongoengine import Document, StringField, DateTimeField, ListField, EmbeddedDocumentField, ObjectIdField
from datetime import datetime
from .picture import Picture
from .track import Track

class Trip(Document):
  id = ObjectIdField(primary_key=True) 
  created = DateTimeField()
  name = StringField()
  tracks = ListField(EmbeddedDocumentField(Track))
  pictures = ListField(EmbeddedDocumentField(Picture))
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
      'tracks': [track.to_map() for track in self.tracks],
      'pictures': [picture.to_map() for picture in self.pictures]
    }
    if self.id:  # Agregar el campo id si está presente en el documento
      map_data['id'] = self.id
    return map_data