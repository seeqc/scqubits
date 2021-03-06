# test_zeropi.py
# meant to be run with 'pytest'
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

import scqubits as qubit
import scqubits.settings
from scqubits import ZeroPi, FileType
from scqubits.tests.conftest import StandardTests

scqubits.settings.FILE_FORMAT = FileType.h5


class TestZeroPi(StandardTests):
    @classmethod
    def setup_class(cls):
        cls.qbt = None
        cls.qbt_type = ZeroPi
        cls.file_str = 'zeropi'
        cls.grid = qubit.Grid1d(1, 2, 3)
        cls.op1_str = 'n_theta_operator'
        cls.op2_str = 'i_d_dphi_operator'
        cls.param_name = 'flux'
        cls.param_list = np.linspace(0, 0.5, 15)
