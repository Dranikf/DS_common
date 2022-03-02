# Work with emissions

def get_frame_quantiles_25_75(col):
    '''The function returns 25 and 75 persentiles of getted column'''
    descr = col.describe()
    return {'25%' : descr['25%'], '75%' : descr['75%']}