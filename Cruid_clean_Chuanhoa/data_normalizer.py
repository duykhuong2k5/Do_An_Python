import pandas as pd

class Normalizer:
    def __init__(self, data_frame):
        """Initialize the Normalizer with the provided DataFrame."""
        self.data_frame = data_frame

    def min_max_scale(self, columns):
        """Normalize specified columns to a range between 0 and 1."""
        for column in columns:
            if column in self.data_frame.columns:
                min_val = self.data_frame[column].min()
                max_val = self.data_frame[column].max()
                if max_val != min_val:
                    self.data_frame[column] = (self.data_frame[column] - min_val) / (max_val - min_val)
                else:
                    self.data_frame[column] = 0  # if min and max are the same, set all values to 0

    def z_score_standardize(self, columns):
        """Standardize specified columns to have a mean of 0 and standard deviation of 1."""
        for column in columns:
            if column in self.data_frame.columns:
                mean = self.data_frame[column].mean()
                std_dev = self.data_frame.column.std()
                if std_dev != 0:
                    self.data_frame[column] = (self.data_frame[column] - mean) / std_dev
                else:
                    self.data_frame[column] = 0  # if std_dev is 0, set all values to 0