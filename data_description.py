# couple of funcitons for getting description of data

import pandas as pd
import numpy as np

def get_col_av_values(col):
    '''get availible values in getted column'''
    # input:
    # col - pandas.DataFrame column wich should be used
    # output:
    # str line wich describe column ranges or couple of levels
    if pd.api.types.is_numeric_dtype(col):
        return "[" + str(np.min(col)) + ";" + str(np.max(col)) + ']'
    if pd.api.types.is_datetime64_any_dtype(col):
        return "[" + np.min(col).strftime("%d.%m.%Y") + ";" +\
                np.max(col).strftime("%d.%m.%Y") + ']'
    else:
        return str(col.unique().tolist())[1:-1].replace("'", "")