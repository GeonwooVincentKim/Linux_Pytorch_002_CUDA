# wsgi.py
import torch
from smart_getenv import getenv

from .app import create_app
from .classifier import Classifier


# Read Parameter-File of routes
# in Environment-Variable.
prm_file = getenv("PRM_FILE", default="/taco_burrito.prm")

# Read Parameter-Files.
params = torch.load(prm_file,
                    map_location=lambda storage, loc: storage)

# Generate an application
# that contains Classifier and Flask.
classifier = Classifier(params)
app = create_app(classifier)
