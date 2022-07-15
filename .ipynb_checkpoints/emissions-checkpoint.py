import numpy as np

# this file represents several of fucntions wich
# can be used for emissions management

def get_frame_quantiles_25_75(col):
    '''The function returns 25 and 75 persentiles of getted column
    inputs:
        col - column which persentiles to be computed
    output:
        {'25%': <25th persentile>, "75%":<75th persentile>}
    '''
    descr = col.describe()
    return {'25%' : descr['25%'], '75%' : descr['75%']}


def get_selcond_emiss_25_75(col, constant = 1.5, cut_type = "both" ):
    '''Funciton for getting selection condition from 
    column, which that will get rid of the emissions.
    According with rule: https://ru.wikipedia.org/wiki/%D0%92%D1%8B%D0%B1%D1%80%D0%BE%D1%81_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0),
    
    inputs:
        col - pandas.Series column which emissions needs to be cleared
        constan - int which adjusts the width of the deleted interval
        but_type -    "left": deletes only left tale;
                      "right": deletes only right tale;
                      "both": deletes both tales (default value).
    outputs:
        pd.Seires with boolean type - False if the observation interpreted as an emission
                                      else True 
    '''

    result = np.ones(col.shape).astype('bool')
    quant = get_frame_quantiles_25_75(col)

    range_25_75 = quant['75%'] - quant['25%']

    if (cut_type == "right") | (cut_type == "both"):
        result = result & (col <= (quant['75%'] + range_25_75 * constant))
    if (cut_type == "left") | (cut_type == "both"):
        result = result & (col >= (quant['25%'] - range_25_75 * constant))

    result[col.isna()] = True

    return result