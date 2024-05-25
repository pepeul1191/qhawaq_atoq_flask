#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback
from flask import Blueprint, request
from admin.models import Member
from admin.database import db_connect, to_dict
from admin.helpers.trip_helper import get_image_metadata

api = Blueprint('api-trip', __name__)

@api.route('/trip/save', methods=['POST'])
def save():
  try:
    _id = request.form['_id']
    #print(_id)
    name = request.form['name']
    #print(name)
    tracks = request.form['tracks']
    #print(tracks)
    images = request.files.getlist('images')
    #print(images)
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