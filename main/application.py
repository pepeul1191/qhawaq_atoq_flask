# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def hello_world():
  return 'Hola Mundo???'
