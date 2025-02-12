import pandas as pd
import numpy as np

def prepare_matrix():
    """
    Args : None
    Objective : imports and intialize matrix
    Returns : Matrix
    """

    taxi_data = pd.read_csv('chicago-taxi-rides.csv')
    taxi_data_cleaned = taxi_data.dropna()

    taxi_mat = np.zeros(shape=(77,77))
    for idx in range(taxi_data_cleaned.shape[0]):
        row, col, val = taxi_data_cleaned.iloc[idx,:]
        row, col = int(row -1), int(col -1)
        taxi_mat[row, col] = val
        
    taxi_matrix = pd.DataFrame(taxi_mat)
    
    return (taxi_matrix / taxi_matrix.sum()).to_numpy()


def TrafficRank(iter):
    # value Error
    # if not(0<= iter <=10):
    #     raise ValueError ("Iter value must be between 0 and 10")
    
    b = 0.85
    M = prepare_matrix()
    n = 77
    r = np.ones(n) / n
    
    if iter == 0:
        return  r
    
    for _ in range(iter):
        r_next = b * (M @ r) + (1-b)/ n * np.ones(n)
        r = r_next
    
    return r