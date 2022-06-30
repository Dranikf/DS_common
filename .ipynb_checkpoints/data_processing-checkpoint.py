# funciton for data processing
import pandas as pd


def insert_next(df, col_name, transform_col, new_name = None):
    '''
        Insertion to data frame after given colum
            Inputs:
                df - pandas.DataFrame in which the insertion is required;
                col_name - str the name of the column after which insertion is required;
                transform_col - pandas.Series to be inserted;
                new_name - str name of new column, by default col_name + "_transf" will used.
            Output
                pd.DataFrame with inserted column.
    '''
    if new_name is None:
        new_name = col_name + "_transf"
    
    if new_name in df.columns:
        df[new_name] = transform_col
    else:
        df.insert(
            df.columns.get_loc(col_name) + 1,
            new_name,
            transform_col
        )
    
    return df


def get_num_cond(df):
    '''
        Get condition for selection from pandas.DataFrame numeric data types
            Inputs:
                df - pandas.DataFrame which numeric columns you have to choose;
            Output
                pd.Series contains boolen dtype condition.
    '''
    return df.apply(lambda x: pd.api.types.is_numeric_dtype(x.dtype))