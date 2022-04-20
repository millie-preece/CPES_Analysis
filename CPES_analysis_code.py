# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:36:00 2022

@author: mpree
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.io import loadmat
import pandas as pd




data = pd.read_csv('20240-0001-Data.tsv', sep='\t')

cell = data[["V00232", "V00233", "V00234", "V00245", "V00235", "V00829", "V00830", "V00855"]]

df_describe = pd.DataFrame(cell)
df_describe.describe()
cell.mean()
print(cell.mean())

cell.dropna(subset = ["V00232"], inplace = True)
cell2 = cell[cell[["V00232", "V00233", "V00234", "V00245", "V00235", "V00829", "V00830", "V00855"]].notna()]

##removing values that are ' ' empty
##good thing is that indexes are kept!

cell2 = cell2[cell.V00233 != ' ']
cell2 = cell2[cell.V00232 != ' ']
cell2 = cell2[cell.V00234 != ' ']
cell2 = cell2[cell.V00245 != ' ']
cell2 = cell2[cell.V00235 != ' ']
cell2 = cell2[cell.V00829 != ' ']
cell2 = cell2[cell.V00830 != ' ']
cell2 = cell2[cell.V00855 != ' ']
