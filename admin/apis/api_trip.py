#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback
from flask import Blueprint, request
from admin.database import db_connect
from mongoengine import DoesNotExist
from datetime import datetime
from bson.objectid import ObjectId
from admin.models.picture import Picture
from admin.models.track import Track
from admin.models.trip import Trip

api = Blueprint('api-trip', __name__)

@api.route('/trip/save', methods=['POST'])
def save():
  try:
    tracks = json.loads(request.form['tracks'])
    pictures = json.loads(request.form['pictures'])
    images = request.files.getlist('images')
    trip_id = request.form['_id']
    track_name = request.form['name']
    track_created = tracks[0]['created']
    # save documents in mongodb
    documents_tracks = [Track.from_map(track) for track in tracks]
    documents_pictures = [Picture.from_map(picture) for picture in pictures]
    document_trip = Trip(
      id=trip_id,
      name=track_name,
      created=datetime.fromisoformat(track_created),
      tracks=documents_tracks,
      pictures=documents_pictures,
    )
    db_connect()
    document_trip.save()
    # save images
    for image in images:
      image_name = image.filename
      #print(image_name)
      uploads_folder = os.path.join(os.getcwd(), 'static', 'uploads')
      upload_trip_folder = os.path.join(uploads_folder, trip_id)
      if not os.path.exists(upload_trip_folder):
        os.makedirs(upload_trip_folder)
      image_path = os.path.join(upload_trip_folder, image_name)
      # Guardar o procesar el archivo según sea necesario
      image.save(image_path)
    return ':)'
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
  
@api.route('/trip/<_id>', methods=['GET'])
def get_user(_id):
  try:
    db_connect()
    print('++++++++++++++++++++++++')
    trip = Trip.objects.get(id=ObjectId(_id))
    trip_dicc = trip.to_map()
    return json.dumps(trip_dicc), 200
  except DoesNotExist:
    return json.dumps({"error": "Document not found"}), 404
  except Exception as e:
    traceback.print_exc()
    return json.dumps({"error": str(e)}), 400