from mongoengine import Document, StringField, DateTimeField, ListField, EmbeddedDocumentField, ObjectIdField
from bson import ObjectId
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
      id=ObjectId(map.get('_id')) if map.get('_id') else None,
      created=datetime.fromisoformat(map['created']),
      name=map['name'],
      tracks=[Track.from_map(track_map) for track_map in map.get('tracks', [])]
    )

  def to_map(self):
    map_data = {
      '_id': str(self.id),
      'created': self.created.isoformat(),  # Sin almacenar como una lista
      'name': self.name,  # Sin almacenar como una lista
      'tracks': [track.to_map() for track in self.tracks],  # Sin almacenar como una lista
      'pictures': [picture.to_map() for picture in self.pictures],  # Sin almacenar como una lista
    }
    return map_data