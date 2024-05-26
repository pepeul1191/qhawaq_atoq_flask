from mongoengine import Document, StringField

class Member(Document):
  id = StringField(primary_key=True) 
  names = StringField()
  last_names = StringField()
  resume = StringField()
  image_url = StringField()
  meta = {
    'collection': 'members'  # Nombre de la colección a la que deseas mapear
  }
