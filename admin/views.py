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
  
@view.route('/admin', methods=['GET'])
def admin():
  locals = {}
  locals['title'] = 'Admin'
  locals['csss'] = []
  locals['jss'] = ['assets/js/app']
  return render_template('admin.html', locals = locals)