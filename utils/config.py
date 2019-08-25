import os
import tensorflow as tf

DATAFOLDER = os.path.join(os.getcwd(),"data")

SVM_PARAM  =  [
    {"e" : 0.5 , "s" : 0.5, "c" : 100},
    {"e" : 1 , "s" : 1, "c" : 100},
    {"e" : 0.5 , "s" : 1, "c" : 500},
    {"e" : 0.5 , "s" : 1, "c" : 1000},
]

OPTIMIZER = [
                tf.keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0) ,
                tf.keras.optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False),
                tf.keras.optimizers.Adagrad(lr=0.01, epsilon=None, decay=0.0),
                tf.keras.optimizers.Adadelta(lr=0.2, rho=0.95, epsilon=None, decay=0.0),
                tf.keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
                tf.keras.optimizers.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0),
                tf.keras.optimizers.Nadam(lr=0.005, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)
            ]
