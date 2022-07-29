from sklearn.metrics import roc_curve
import plotly.graph_objects as go

def pltl_roc_by_preds(y_true, y_score, skl_roc_kwargs = {}, pltl_scatter_kwargs = {}):
    '''
        Plotly figure for ROC.
        Input:
            y_true - ndarray of shape (n_samples,) real classes;
            y_score - ndarray of shape (n_samples,) predicted probability;
            skl_roc_kwargs - dict with arguments for sklearn.metrics.roc_curve
                             function https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html;
            pltl_scatter_kwargs - dict with arguments for plotly.graph_objects.Scatter funciton
                                    https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html
        Output plotly.graph_objs._scatter.Scatter wich contains roc curve.
    '''
    
    fpr, tpr, tresholds = roc_curve(y_true, y_score, **skl_roc_kwargs)
    return go.Scatter(x = fpr, y = tpr, **pltl_scatter_kwargs)