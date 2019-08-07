import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas


class Plotter(object):
    """docstring for Plotter."""

    def __init__(self, data):
        """
            data should be a pandas dataframe
        """
        super(Plotter, self).__init__()
        self.data = data


    def plot_wind(self, year, segment):

        seg_data = data[year][segment[0], segment[1]]
        plt.plot(seg_data)
        plt.show()
        
        return None
