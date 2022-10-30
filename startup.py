#!/usr/bin/env python
"""
This module is used configurate the IPython startup profile, it configures autoreload of
modules and import user favorite libraries.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Victor Vinci Fantucci"
__email__ = "victor.v.fantucci@gmail.com"
__date__ = "2022/10/30"
__license__ = "GPLv3"
__maintainer__ = "VictorFantucci"

# Analysis and organization of data
import pandas as pd
import numpy as np

# Pandas options
pd.options.display.max_columns = 30
pd.options.display.max_rows = 20

# Visualization
import matplotlib.pyplot as plt

# Get ipython
from IPython import get_ipython
ipython = get_ipython()

# If in ipython, load autoreload extension
if 'ipython' in globals():
    print('\nWelcome to IPython!')
    ipython.run_line_magic('load_ext', 'autoreload')
    ipython.run_line_magic('autoreload' , '2')

# Display all cell outputs in notebook
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

print('Your favorite libraries have been loaded.')
