from mongoengine import connect

def to_dict(document):
  tmp = document.to_mongo().to_dict()
  if '_id' in tmp:
    tmp['_id'] = str(document.id)
  return tmp

def db_connect():
  connect(
    db='atoq',
    username='',
    password='',
    host='localhost',
    port=27017
  )