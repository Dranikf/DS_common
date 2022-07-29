import numpy as np

# functions for simplify plotting aspects

def get_meshtraces(mesh):
    '''
        Return traces for plotly from np.mesh.
            Inputs:
                mesh - one of matrix that np.mesh returns;
            Output list with np.arrays traces in format [i_ind, j_ind, k_ind]
    '''

    i_ind = np.array([])
    j_ind = np.array([])
    k_ind = np.array([])

    for x in range(mesh.shape[1]-1):
        for y in range(mesh.shape[0]-1):
            i_ind = np.append(i_ind, x + (mesh.shape[1])*y)
            j_ind = np.append(j_ind, x + (mesh.shape[1])*(y+1))
            k_ind = np.append(k_ind, (x+1) + (mesh.shape[1])*(y+1))
            
            i_ind = np.append(i_ind, x + (mesh.shape[1])*y)
            j_ind = np.append(j_ind, x+1 + (mesh.shape[1])*(y))
            k_ind = np.append(k_ind, (x+1) + (mesh.shape[1])*(y+1))

    return [i_ind, j_ind, k_ind]



def pltl_dual_side_arrow(
    x, y, 
    double_kwargs = {
        'xref' : "x", 'yref' : "y", 
        'axref' : "x", 'ayref' : "y",
         "arrowhead" : 3
    }, 
    nose_kwargs = {}, tail_kwargs = {}
):
    '''
        Get list of annotations wich helps to build dual side arrows.
            Inputs:
                x - list whith two elements `[x of nose, x of tail]`;
                y - list with two elements `[y of nose, y of tail]`.
            Output - list of dictionaries which is to be used as `annotations`
            argument in figure.update_layout function.
    '''
    
    # dictionary association with priority for the dict
    # of the particular side (https://favtutor.com/blogs/merge-dictionaries-python)
    nose_kwargs = {**double_kwargs, **nose_kwargs}
    tail_kwargs = {**double_kwargs, **tail_kwargs}
    
    return [
        dict(
            x = x[0], y = y[0], ax = x[1], ay = y[1], **nose_kwargs
        ),
        dict(
            x = x[1], y = y[1], ax = x[0], ay = y[0], **tail_kwargs
        )
    ]