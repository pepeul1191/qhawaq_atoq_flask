#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from flask import Blueprint, request
from admin.models import Member
from admin.database import db_connect, to_dict

api = Blueprint('api-trip', __name__)

@api.route('/trip/save', methods=['POST'])
def save():
  try:
    name = request.form['name']
    print(name)
    print(request.files)
    images = request.files.getlist('images')
    for image in images:
      image_name = image.filename
      print(image_name)
      image_path = os.path.join('/home/pepe/Documentos/python/atoq_back/static/uploads/', image_name)
        # Guardar o procesar el archivo según sea necesario
      image.save(image_path)
    return ':)'
  except Exception as e:
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500