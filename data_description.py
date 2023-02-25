# couple of funcitons for getting description of data

import pandas as pd
import numpy as np

from statsmodels.distributions.empirical_distribution import ECDF
from sklearn import metrics

def get_col_av_values(col):
    '''
        Get availible values in getted column. Makes different
        for numeric dtypes and others. 
        For numeric dtypes returns range like "[min, max]".
        For non-numeric dtypes returns possible values. 
        input:
            col - pandas.Series, column wich values should be returned;
        output:
            str, line wich describe column ranges or couple of levels
    '''
    if pd.api.types.is_numeric_dtype(col):
        return "[" + str(np.min(col)) + ";" + str(np.max(col)) + ']'
    elif pd.api.types.is_datetime64_any_dtype(col):
        return "[" + np.min(col).strftime("%d.%m.%Y") + ";" +\
                np.max(col).strftime("%d.%m.%Y") + ']'
    else:
        return str(col.unique().tolist())[1:-1].replace("'", "")
    
    
def get_col_obj_unique_count(col):
    '''
        For non-numeric pandas.Series, returns a count of unique values. 
        For numeric variables returns "-".
        input:
            col - pandas.Series column which unique values should be returned;
        output:
             "-" for numeric dtype and number of levels for other types.
    '''
    if pd.api.types.is_numeric_dtype(col) or\
       pd.api.types.is_datetime64_any_dtype(col):
        return "-"
    else:
        return len(col.unique())
    
def get_Dran_col_descr(col):
    '''
        Return the panas.Series most complete
        description specified for me.
        input:
            col - pandas.Series, which should be descripted;
        output:
            pandas.Series wich contains:
                - Series dtype;
                - Availible values (product of get_col_av_values function);
                - For non numeric series count of levels 
                   (product of get_col_obj_unique_count function);
                - Count of values that contains np.NaN.
    '''
    return pd.Series(
        [
            col.dtype, 
            get_col_av_values(col), 
            get_col_obj_unique_count(col), 
            sum(col.isna())
        ],
        index = ["type", "unique values", "unique count", "nan count"]
    )

def get_most_freq_by_cond(ser, cond):
    '''
        Returns value from series which has the 
        most frequent manifestation of the trait 
        specified in cond.
        Inputs:
            ser - pandas.Series with size n_sample 
                    which value must be selected;
            cond - pandas.Series of bool dtype, condition 
                    which helps select values with the manifestation of the trait;
        Output: required value from ser.
            
    '''
    return (ser[cond].value_counts()/ser.value_counts()).idxmax()



def ECDFs_by_classes(
    val_col, classes_markers, 
    side = "right", functions = False
):
    '''
        statsmodels.distributions.empirical_distribution.ECDF wrapper which
        allows to build different ecdfs for different classes.
        inputs:
            val_col - np.array, which will used as argument of ecdfs;
            classes_markers - np.array, which allows us to divide observations into classes;
            side - str or list, defines the shape of the intervals constituting the steps. 
                                ‘right’ correspond to [a, b) intervals and ‘left’ to (a, b].
            functions - bool, defines the type of the result, 
                              it can be computed values or functions.
         output:
             dictionary where keys is markers, values is ecdfs.
    '''
    unique_markers = np.unique(classes_markers)
    
    res = {}
    if (not hasattr(side, "__iter__")) | (type(side) == str):
        side = [side]*len(unique_markers)
    
    for i, cm in enumerate(unique_markers):
        ecdf = ECDF(val_col[classes_markers == cm], side = side[i])
        res[cm] = ecdf if functions else ecdf(val_col)
        
    return res


def conf_table(y_true, y_pred, thresholds = None):
    '''
    Returns table that contains the information from confusion
    matrix, but for given thresholds.
    Input:
        y_true - np.array real labels of classes 
                 for observations (1-positive, 0-negative);
        y_pred - np.array predicted probabilities that 
                 observations belongs to positive class;
        thresholds - list of thresholds for wich confusion
                     matrix should be computed. By default None, 
                     and will use same array as y_pred;
    Output:
        pandas.DataFrame - which contains TN, FP, FN, TP 
                           and relvant rates.
    '''

    if type(thresholds) == type(None):
        thresholds = np.sort(y_pred)

    res_frame = pd.DataFrame(
        list(map(
            lambda p: metrics.confusion_matrix(y_true, y_pred > p).ravel(),
            thresholds
        )),
        index = thresholds,
        columns = ["TN", "FP", "FN", "TP"]
    )
    res_frame.index.name = "treshold"

    N = res_frame["FP"] + res_frame["TN"]
    res_frame["TNR"] = res_frame["TN"]/N
    res_frame["FPR"] = res_frame["FP"]/N

    P = res_frame["TP"] + res_frame["FN"]
    res_frame["FNR"] = res_frame["FN"]/P
    res_frame["TPR"] = res_frame["TP"]/P

    return res_frame

ru_scoring_rename_rule = {
    "TN" : "Верно выданные (шт.)",
    "FP" : "Ошибочно удержанные (шт.)",
    "FN" : "Ошибочно выданные (шт.)",
    "TP" : "Верно удержанные (шт.)",
    "TNR" : "Верно выданные (% от хороших)",
    "FPR" : "Ошибочно удержанные (% от хороших)",
    "FNR" : "Ошибочно выданные (% от дефолта)",
    "TPR" : "Верно удержанные (% от дефолта)"
}