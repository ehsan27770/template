import tensorflow as tf
from tensorflow import keras

class CustomLoss(object):
    """docstring for CustomLoss.
    for complete documentation of custom loss check out :
        https://keras.io/api/losses/
    any callable object with signature fn(y_true,y_pred) can be used as a loss
    function here I used a callable class(with magic method __call__) instead of
    normal function
    """

    def __init__(self):
        super(CustomLoss, self).__init__()
        
    def __call__(self, y_true, y_pred):
        pass
