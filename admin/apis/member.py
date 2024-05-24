#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint
from admin.models import Member
from admin.database import db_connect, to_dict

api = Blueprint('api-member', __name__)

@api.route('/member/list', methods=['GET'])
def list():
  try:
    db_connect()
    members = Member.objects()
    return json.dumps([to_dict(member) for member in members])
  except Exception as e:
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500