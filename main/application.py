# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from .blueprints import register

APP = Flask(__name__)

register(APP)
