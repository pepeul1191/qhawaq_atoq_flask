#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Blueprint, render_template

view = Blueprint('acces-view', __name__, template_folder='./templates')

@view.route('/login', methods=['GET'])
@view.route('/sign-in', methods=['GET'])
@view.route('/reset-password', methods=['GET'])
def index():
  locals = {}
  locals['title'] = 'Login'
  locals['csss'] = ['dist/login']
  locals['jss'] = ['dist/login']
  return render_template('access.html', locals = locals)