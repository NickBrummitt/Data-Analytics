# Program will be given a list with 9 elements. That list should be converted to a 3x3 matrix.
# An exception should be reached if the list does not consist of 9 elements
# Output should consist of a dictionary of lists.

import numpy as np


def calculate(list):
    # Create try-except statement for input list containing less than 9 elements
    try:
        # Try to create 3x3 matrix from list
        m = np.array(list)
        m = m.reshape(3, 3)
    except Exception as ex:
        raise ValueError("List must contain nine numbers.") from None

    # Create calculations dictionary with the following corresponding values:
    #         {
    #         'mean': [axis1, axis2, flattened],
    #         'variance': [axis1, axis2, flattened],
    #         'standard deviation': [axis1, axis2, flattened],
    #         'max': [axis1, axis2, flattened],
    #         'min': [axis1, axis2, flattened],
    #         'sum': [axis1, axis2, flattened]
    #         }

    calculations = {
        'mean': [np.mean(m, axis=0).tolist(), np.mean(m, axis=1).tolist(), np.mean(m.flatten()).tolist()],
        'variance': [np.var(m, axis=0).tolist(), np.var(m, axis=1).tolist(), np.var(m.flatten()).tolist()],
        'standard deviation': [np.std(m, axis=0).tolist(), np.std(m, axis=1).tolist(), np.std(m.flatten()).tolist()],
        'max': [np.max(m, axis=0).tolist(), np.max(m, axis=1).tolist(), np.max(m.flatten()).tolist()],
        'min': [np.min(m, axis=0).tolist(), np.min(m, axis=1).tolist(), np.min(m.flatten()).tolist()],
        'sum': [np.sum(m, axis=0).tolist(), np.sum(m, axis=1).tolist(), np.sum(m.flatten()).tolist()]
        }

    return calculations
