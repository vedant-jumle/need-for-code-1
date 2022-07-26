import tensorflow as tf
from tensorflow import keras
import numpy as np

class CareerAdvisor:
    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)

    