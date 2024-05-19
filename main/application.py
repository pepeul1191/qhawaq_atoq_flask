# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from .blueprints import register
from .helpers import scripts, styles
from .constants import CONSTANTS

APP = Flask(
  __name__,
  static_folder='../static',
  static_url_path='/'
)

# filters/helpers in templates
@APP.context_processor
def utility_processor():
  return dict(
    styles=styles,
    scripts=scripts,
    constants=CONSTANTS,
  )

register(APP)
