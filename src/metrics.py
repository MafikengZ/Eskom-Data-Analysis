import numpy as np
from .preprocessing import DataProcessing


class Metrics:
    def __init__(self,data):
        self.data = data
        
    def summery_stats (self):

         metrics = {
                'mean': np.mean(data),
                'median': np.median(data),
                'var': np.var(data , ddof=1),
                'std': np.std(data , ddof=1),
                'min': np.min(data),
                'max': np.max(data)}

        output = dict()
        for key , values in metrics.items():
            output[key] = round(values,2)
        return output

    def five_num_summary(data):

        metrics = {
                'max': np.max(items),
                'median': np.median(items),
                'min': np.min(items),
                'q1': np.percentile(items, 25),
                'q3': np.percentile(items , 75)
    }
    
    return metrics


