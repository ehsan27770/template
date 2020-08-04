import tensorflow as tf
from tensorflow import keras

class CustomCallback(keras.callbacks.Callback):
    """docstring for CustomCallback.

    for complete documentation of custom callback check out :
        https://keras.io/guides/writing_your_own_callbacks/
        https://keras.io/api/callbacks/

    'self.model' can be used to obtain parameters of the model
    e.g. 'self.model.optimizer.learning_rate'"""

    def __init__(self):
        super(CustomCallback, self).__init__()


    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        pass

    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        pass

    def on_test_begin(self, logs=None):
        pass

    def on_test_end(self, logs=None):
        pass

    def on_predict_begin(self, logs=None):
        pass

    def on_predict_end(self, logs=None):
        pass

    def on_train_batch_begin(self, batch, logs=None):
        pass

    def on_train_batch_end(self, batch, logs=None):
        pass

    def on_test_batch_begin(self, batch, logs=None):
        pass

    def on_test_batch_end(self, batch, logs=None):
        pass

    def on_predict_batch_begin(self, batch, logs=None):
        pass

    def on_predict_batch_end(self, batch, logs=None):
        pass
