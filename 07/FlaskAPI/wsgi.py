# wsgi.py
import torch
from smart_getenv import getenv

from .app import create_app
from .app.classifier import Classifier


