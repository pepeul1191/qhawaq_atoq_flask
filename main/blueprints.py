#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .views import view as main_blueprints
from demo.blueprints import blueprints as demo_blueprints
from admin.blueprints import blueprints as admin_blueprints

def register(app):
  # append sub blueprints
  modules_blueprints = []
  print('------------------------')
  modules_blueprints.append(admin_blueprints)
  modules_blueprints.append(demo_blueprints)
  # load main blueprint to app
  app.register_blueprint(main_blueprints)
  # load sub blueprints to app
  for blueprints in modules_blueprints:
    for blueprint in blueprints:
      app.register_blueprint(blueprint)
  # register oauth
  # app.register_blueprint(oauth_view)
  # registar error/access/:code
  # app.register_blueprint(error_view)
