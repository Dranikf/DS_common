# couple of funcitons for getting description of data

import pandas as pd
import numpy as np

def get_col_av_values(col):
    '''get availible values in getted column'''
    # input:
    # col - pandas.Series column wich should be used
    # output:
    # str line wich describe column ranges or couple of levels
    if pd.api.types.is_numeric_dtype(col):
        return "[" + str(np.min(col)) + ";" + str(np.max(col)) + ']'
    if pd.api.types.is_datetime64_any_dtype(col):
        return "[" + np.min(col).strftime("%d.%m.%Y") + ";" +\
                np.max(col).strftime("%d.%m.%Y") + ']'
    else:
        return str(col.unique().tolist())[1:-1].replace("'", "")
    
    
def get_col_obj_count(col):
    '''
        for categorial variables returns a couple of levels,
        for numeric variables returns ranges
    '''
    # input:
    # col - pandas.Series column wich should be used
    # output:
    # for numeric variable "-" and number of levels for categorial
    
    if pd.api.types.is_numeric_dtype(col) or\
        pd.api.types.is_datetime64_any_dtype(col):
        return "-"
    else:
        return len(col.unique())
    
def get_columns_desription(df):
    '''
        get a full discription of pandas.DataFrame
        with Data types, ranges, Levels_number, NA_counts 
    '''
    # input:
    # df - pandas.DataFrame to which you want to apply the function
    # output
    # pandas.DataFrame with input columns in index
    #      and characteristics in columns
    
    result = pd.DataFrame(columns = [
        'Data type', 
        'Range',
        'Levels number',
        'NA count'
    ])
    
    for col in df.columns:
        result.loc[col, :] = [
            df[col].dtype,
            get_col_av_values(df[col]),
            get_col_obj_count(df[col]),
            sum(df[col].isna())
        ]
    
    return result