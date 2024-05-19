#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint
from sqlalchemy.orm import sessionmaker
from main.database import engine
from demo.models import Level

api = Blueprint('demo-api-index', __name__)

@api.route('/demo/list', methods=['GET'])
def list():
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    # Consultar todos los registros de la tabla Level
    levels = session.query(Level).all()
    return json.dumps([level.to_dict() for level in levels])
  except Exception as e:
    # Manejar cualquier otro error
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
  finally:
    session.close()