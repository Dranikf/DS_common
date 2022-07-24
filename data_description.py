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

def get_most_freq_by_cond(ser, cond):
    '''
        Returns value from series which has the 
        most frequent manifestation of the trait 
        specified in cond
        Inputs:
            ser - pandas.Series with size n_sample 
                    which value must be selected;
            cond - condition which helps select values 
                    with the manifestation of the trait;
        Output required value from ser.
            
    '''
    return (ser[cond].value_counts()/ser.value_counts()).idxmax()

def np_replace(arr, rule):
    '''
        Replacing funciton for numpy array.
        Inputs:
            arr - numpy array to be transformed;
            rule - rule as dict.
        Output trancfromed numpy array.
    '''
    rule_values = np.array(list(rule.values()))
    rule_keys = np.array(list(rule.keys()))
        
    replacer = lambda key: rule_values[key == rule_keys][0] if np.any(key == rule_keys) else key
        
    return np.array(list(map(replacer, arr.ravel()))).reshape(arr.shape)