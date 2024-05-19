#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .views import view as main_blueprints

def register(app):
  modules_blueprints = []
  # register blueprint of apps
  modules_blueprints.append(main_blueprints)
  # cargar blueprints a app
  for blueprint in modules_blueprints:
    app.register_blueprint(blueprint)
  # register oauth
  # app.register_blueprint(oauth_view)
  # registar error/access/:code
  # app.register_blueprint(error_view)
