# -*- coding: utf-8 -*-

"""
Copyright 2015-Present Randal S. Olson

This file is part of the TPOT library.

The TPOT library is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

The TPOT library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details. You should have received a copy of the GNU General Public License along
with the TPOT library. If not, see http://www.gnu.org/licenses/.

"""

from .base import TPOTBase
from .config_classifier import classifier_config_dict
from .config_regressor import regressor_config_dict


class TPOTClassifier(TPOTBase):
    """TPOT estimator for classification problems"""

    scoring_function = 'accuracy'  # Classification scoring
    default_config_dict = classifier_config_dict # Classification dictionary
    classification = True
    regression = False


class TPOTRegressor(TPOTBase):
    """TPOT estimator for regression problems"""

    scoring_function = 'neg_mean_squared_error'  # Regression scoring
    default_config_dict = regressor_config_dict # Regression dictionary
    classification = False
    regression = True
