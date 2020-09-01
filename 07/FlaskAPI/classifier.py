# classifier.py
from torch import nn, optim
from torchvision import transforms, models


def create_network():
    # Read 'resnet18'.
    # You don't need to set 'pretrained=True'
    # because the Parameter set behind of model.
    net = models.resnet18()

    # Convert Last-Layer as 2-Output of Linear-Layer.
    fc_input_dim = net.fc.in_features
    net.fc = nn.Linear(fc_input_dim, 2)
    return net
