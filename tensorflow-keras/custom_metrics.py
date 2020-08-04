import tensorflow as tf
from tensorflow import keras

class CustomMetric(object):
    """docstring for CustomMetric.
    for complete documentation of custom metrics check out:
        https://keras.io/api/metrics/
    it is possible to define a metric as a stateless function or as a statefull
    subclass of tensorflow.keras.metrics.Metric
    """

    def __init__(self):
        super(CustomMetric, self).__init__()

    def update_state(self, y_true, y_pred):
        pass

    def result(self):
        pass

    def reset_states(self):
        pass
