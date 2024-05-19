#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .views import view as main_blueprints
from .demo.blueprints import blueprints as demo_blueprints

def register(app):
  modules_blueprints = []
  modules_blueprints.append(demo_blueprints)
  # cargar blueprints a app
  for blueprints in modules_blueprints:
    for blueprint in blueprints:
      app.register_blueprint(blueprint)
  app.register_blueprint(main_blueprints)
  # register oauth
  # app.register_blueprint(oauth_view)
  # registar error/access/:code
  # app.register_blueprint(error_view)
