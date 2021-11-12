import pandas  as pd
import numpy as np


class DataProcessing:
    def __init__(self,data):

        self.data = pd.read_csv(data)

   @staticmethod
   def electric_by_province():

        for col , row in self.data.iloc[:,1:].items():
            df[col] = self.data.[col].str.replace(',' , '')
        return self.data

    @staticmethod
    def twitter_df(self):
        return self.data



