#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Blueprint, render_template

view = Blueprint('demo-view-index', __name__, template_folder='./../templates')

@view.route('/demo', methods=['GET'])
def index():
  locals = {}
  locals['title'] = 'Demo'
  locals['csss'] = ['bootstrap', 'fontawesome']
  locals['jss'] = ['jquery', 'app']
  return render_template('demo.html', locals = locals)
