def model(k, alpha, beta, gamma):
    """Returns values of alpha-beta-gamma model at given k values

    Parameters
    ----------
    k : array-like

    alpha, beta, gamma : float
        Parameters of model
    """


def residuals(pars, data):
    """Returns data - model for given values of parameters

    Parameters
    ----------
    pars : array-like
        [alpha, beta, gamma] parameters.

    data : Data object
        Data to be compared with model.
    """

    return data.y - model(k, *pars)

def objective(pars, data):
    """Objective function to miminize
    """
    
    return ((residuals(*pars, data)**2 / data.uncertainty**2).sum()

def get_best_fit():
    """Compute best-fit model parameters


    Returns
    -------
    pars : array-like
        Best-fit [alpha, beta, gamma] parameters 
    """
