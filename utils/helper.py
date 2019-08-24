import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
import scipy
import pandas


class Plotter(object):
    """docstring for Plotter."""

    def __init__(self):
        """
            data should be a pandas dataframe
        """
        super(Plotter, self).__init__()
        # self.data = data


    def plot_wind(self, year, segment):

        seg_data = data[year][segment[0], segment[1]]
        plt.plot(seg_data)
        plt.show()

        return None


    def find_accurracy_on_testset(self, model, X_test, Y_test,clip=False,plot=True):
        results = model.predict(X_test)
        print("-----------------------------------------------------------")
        print("MSE: "+ str(mse(Y_test,results)))
        print("-----------------------------------------------------------")

        if plot:
            if clip:
                fig, ax = plt.subplots(figsize=(16,5))
                ax.plot(Y_test.values[0:100], label='True Value')
                ax.plot(results[0:100],label='Predicted Value')
                ax.set_xticks([])
                ax.legend()
                plt.show()

            else:
                fig, ax = plt.subplots(figsize=(16,5))
                ax.plot(Y_test.values, label='True Value')
                ax.plot(results,label='Predicted Value')
                ax.set_xticks([])
                ax.legend()
                plt.show()



        return None
