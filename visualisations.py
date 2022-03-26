import numpy as np

# functions for simplify plotting aspects

def get_meshtraces(mesh):
    '''return traces for plotly from np.mesh'''
    # inputs:
    # mesh - one of matrix that np.mesh returns
    # output:
    # list with np.arrays traces in format
    # [i_ind, j_ind, k_ind]

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