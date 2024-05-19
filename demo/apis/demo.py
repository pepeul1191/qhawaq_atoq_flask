#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint

api = Blueprint('demo-api-index', __name__)

@api.route('/demo/list', methods=['GET'])
def list():
  data = [
      {
          "nombre": "Juan",
          "edad": 30,
          "ciudad": "Madrid"
      },
      {
          "nombre": "María",
          "edad": 25,
          "ciudad": "Barcelona"
      },
      {
          "nombre": "Luis",
          "edad": 35,
          "ciudad": "Valencia"
      }
  ]
  return json.dumps(data)
