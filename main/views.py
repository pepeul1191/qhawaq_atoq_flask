#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

view = Blueprint('main', __name__)

@view.route('/', methods=['GET'])
def home():
  return 'Home'
