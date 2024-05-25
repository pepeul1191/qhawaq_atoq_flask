#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback
from flask import Blueprint, request
from admin.models import Track, Trip
from admin.database import db_connect, to_dict
from admin.helpers.trip_helper import get_image_metadata
from datetime import datetime

api = Blueprint('api-trip', __name__)

@api.route('/trip/save', methods=['POST'])
def save():
  try:
    tracks = json.loads(request.form['tracks'])
    print(tracks)
    images = request.files.getlist('images')
    trip_id = request.form['_id']
    track_name = request.form['name']
    track_created = tracks[0]['created']
    # save documents in mongodb
    documents_tracks = [Track.from_map(track) for track in tracks]
    document_trip = Trip(
      id=trip_id,
      name=track_name,
      created=datetime.fromisoformat(track_created),
      tracks=documents_tracks
    )
    db_connect()
    document_trip.save()
    # save images
    for image in images:
      image_name = image.filename
      #print(image_name)
      image_path = os.path.join('/home/pepe/Documentos/python/atoq_back/static/uploads/', image_name)
      # Guardar o procesar el archivo según sea necesario
      image.save(image_path)
    return ':)'
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500