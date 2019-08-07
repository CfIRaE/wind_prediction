#get complete data


class Data(object):
    """docstring for Data."""

    def __init__(self):
        super(Data, self).__init__()

    def get_compdata(self, csv_location):
        """
            csv file should me merged before feeding to this function what it will do that it take the csv and return the data frame with some preprocessiong like
            NAN removal,
        """

        df = pd.read_csv()
        return df

    def get_yearwise(self, csv_location):

        """
            return data in the form of dict for each year
            {
                2011 : array([1,2,34,...,342]),
                2012 : array([12,3,4,...,231])
                ...
            }
        """

        return dict_
