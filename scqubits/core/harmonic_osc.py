# harmonic_osc.py
#
# This file is part of scqubits.
#
#    Copyright (c) 2019, Jens Koch and Peter Groszkowski
#    All rights reserved.
#
#    This source code is licensed under the BSD-style license found in the
#    LICENSE file in the root directory of this source tree.
############################################################################

import numpy as np
import scipy as sp

import scqubits.core.operators as op
from scqubits.core.qubit_base import QuantumSystem


def harm_osc_wavefunction(n, x, losc):
    """For given quantum number n=0,1,2,... return the value of the harmonic oscillator wave function
    :math:`\\psi_n(x) = N H_n(x/l_{osc}) \\exp(-x^2/2l_{osc})`, N being the proper normalization factor.

    Parameters
    ----------
    n: int
        index of wave function, n=0 is ground state
    x: float or ndarray
        coordinate(s) where wave function is evaluated
    losc: float
        oscillator length, defined via <0|x^2|0> = losc^2/2

    Returns
    -------
    float
        value of harmonic oscillator wave function
    """
    return ((2.0 ** n * sp.special.gamma(n + 1.0) * losc) ** (-0.5) * np.pi ** (-0.25) *
            sp.special.eval_hermite(n, x / losc) * np.exp(-(x * x) / (2 * losc * losc)))


# —Oscillator class—————————————————————————————————————————————————————————————————————————————————————————————————————

class Oscillator(QuantumSystem):
    """General class for mode of an oscillator/resonator."""

    def __init__(self, omega, truncated_dim=None):
        self._sys_type = 'oscillator'
        self.omega = omega
        self.truncated_dim = truncated_dim

    def eigenvals(self, evals_count=6):
        """Returns array of eigenvalues.

        Parameters
        ----------
        evals_count: int, optional
            number of desired eigenvalues (default value = 6)

        Returns
        -------
        ndarray
        """
        evals = [self.omega * n for n in range(evals_count)]
        return np.asarray(evals)

    def eigensys(self, evals_count=6):
        """Returns array of eigenvalues and eigenvectors

        Parameters
        ----------
        evals_count: int, optional
            number of desired eigenvalues (default value = 6)

        Returns
        -------
        ndarray, ndarray
        """
        evecs = np.zeros(shape=(self.truncated_dim, evals_count), dtype=np.float_)
        np.fill_diagonal(evecs, 1.0)

        return self.eigenvals(evals_count=evals_count), evecs

    def hilbertdim(self):
        """Returns Hilbert space dimension

        Returns
        -------
        int
        """
        return self.truncated_dim

    def creation_operator(self):
        """Returns the creation operator"""
        return op.creation(self.truncated_dim)

    def annihilation_operator(self):
        """Returns the creation operator"""
        return op.annihilation(self.truncated_dim)
