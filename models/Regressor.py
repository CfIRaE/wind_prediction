from __future__ import absolute_import, division, print_function, unicode_literals
import datetime
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np


def getmodel(opt):
    model = tf.keras.Sequential()
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer=opt, loss='mean_squared_error', metrics=["mse","mae"])

    return model

class myCallbacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        print('The mean absolute error for epoch {} is {:7.2f} and mean squared error is {:7.2f}.'.format(epoch, logs['mae'], logs['mse']))
