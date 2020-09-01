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


# Define a class named 'Classifier'.
class Classifier(object):
    def __init__(self, params):
        # Create Discrimination-Network.
        self.net = create_network()

        # Set the parameter of a procedure of training-accomplished
        self.net.load_state_dict(params)

        # Set as Evaluation-Mode.
        self.net.eval()

        # A function that converts Image to the Tensor.
        self.transformer = transforms.Compose([
            transforms.CenterCrop(224),
            transforms.ToTensor()
        ])

        # Connect Classification-ID and Name.
        self.classes = ["burrito", "taco"]

