import pandas as pd # type: ignore
import numpy as np
import time
import matplotlib.pyplot as plt # type: ignore

def calc_self(kernel, macro_xs, inc_E):
    top = 0
    bot = 0
    for i in range(len(kernel)):
        top += kernel[i]*inc_E*macro_xs[i]
        bot += macro_xs[i]
    return top/bot


def comp_fine_mesh(tol, user_bounds, spec_f, nuclide_f):
    '''Returns fine group bounds based on given spectrum'''
    spec = pd.read_csv(spec_f, sep=",", header=0, index_col=0)
    spec = spec.to_numpy()


    E_vec = spec[0, :]
    phi_vec = spec[1, :]

    nuc_dat = pd.read_csv(nuclide_f, delim_whitespace=True, header=0)
    nuc_dat = nuc_dat.to_numpy()

    A = nuc_dat[:, 0]
    frac = nuc_dat[:, 1]
    pot = nuc_dat[:, 2]

    Sigma = frac*pot
    alpha = (1-A**2)/(1+A)**2
    kern = (1-alpha)/2

    bounds = [np.max(E_vec)]
    phi_avg = []

    i = 0
    while i < len(E_vec)-1:
        err = 0
        avg = phi_vec[i]
        sum = maxi = mini = phi_vec[i]
        n = 1
        SELF = calc_self(kern, Sigma, E_vec[i])
        while err < tol and i < len(E_vec)-1 and E_vec[i] > user_bounds[0] and bounds[-1]-E_vec[i] <= SELF:
            i += 1
            n += 1
            sum += phi_vec[i]
            avg = sum / n
            if phi_vec[i] > maxi:
                maxi = phi_vec[i]
            if phi_vec[i] < mini:
                mini = phi_vec[i]
            err1 = np.abs((phi_vec[i] - avg))/avg
            err2 = np.abs((mini - avg))/avg
            err3 = np.abs((maxi - avg))/avg
            err = max(err1, err2, err3)
        if E_vec[i] <= user_bounds[0]:
            user_bounds.pop(0)
            if len(user_bounds) == 0:
                user_bounds = [-1]
        bounds.append(E_vec[i])
        phi_avg.append(avg)

    return E_vec, phi_vec, bounds, phi_avg


