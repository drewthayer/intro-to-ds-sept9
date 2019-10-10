import numpy as np

def normalize_array(arr):
    ''' normalize the array (subtract mean, divide by stdev)
    input: a 1-D numpy array

    output: a 1-D numpy array
    '''
    mean = arr.mean()
    stdev = arr.std()
    norm = (arr - mean) / stdev

    return norm


def make_filled_array(num_rows, num_cols, fill_val=5):
    '''
    return an array of input dimensions filled with fill val
    '''
    return np.ones((num_rows, num_cols)) * fill_val


def replace_biggest_with_zero(arr):
    ''' replace the largest element in arr with 0 '''
    idx = arr.argmax()
    arr[idx] = 0

    return arr

def get_samples(arr, n, replace=True):
    return np.random.choice(arr, n, replace=replace)



# run the functions
array = np.array([1,5,3,8,2,400])

norm = normalize_array(array)

filled = make_filled_array(num_rows=3, num_cols=4, fill_val=2)

replaced = replace_biggest_with_zero(array)

samples = get_samples(array, 3)
