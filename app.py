#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.07.24   17:51
-------------------------------------------------------------------------------
   @Change:   2020.07.24
-------------------------------------------------------------------------------
"""

from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    configure_app(app)
    return app


def configure_app(app, config=Config):
    app.config.from_object(config)

