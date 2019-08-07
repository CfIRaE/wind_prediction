from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense


def basic_lstm():

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    return model
