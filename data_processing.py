# funciton for data processing
import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder


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



def pd_OHE(df, sk_OHE_kwarg = {}):
    '''
        One hot encoding for pandas.DataFrame. Result type steel
        pandas.DataFrame and columns have readable names, in fomat colname_catname.
            Inputs:
                df - pandas.DataFrame for one hot encoding;
                sk_OHE_kwags - dict which contains sklearn.preprocessing.OneHotEncoding arguments.
            Output pandas.DataFrame with incoed features.
    '''
    
    def name_cat(cats, name, drop_idx = None):
        '''
            For givent categoryes and name
            returns list of strings "category_name" with
            len of cats array
        '''
        # if some columns droped we need to delete related
        # category from columns names
        if not drop_idx is None:
            cats = np.delete(cats, drop_idx)
            
        return list(map(lambda x: name + "_" + str(x), cats))
    
    sk_OHE_kwarg["sparse"] = False
    my_ohe = OneHotEncoder(**sk_OHE_kwarg).fit(df)
    
    columns = []
    for i in range(len(my_ohe.categories_)):
        if not my_ohe.drop_idx_ is None:
            columns += name_cat(my_ohe.categories_[i], df.columns[i], drop_idx = my_ohe.drop_idx_[i])
        else:
            columns += name_cat(my_ohe.categories_[i], df.columns[i])
    
    return pd.DataFrame(my_ohe.transform(df), columns = columns, index = df.index)