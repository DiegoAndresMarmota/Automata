# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:33:34 2023

@author: DiegoAndresMarmota
"""

import numpy as np
import pandas as pd
#import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
from scipy.stats import skew, kurtosis, chi2



#Variables_inputs
decimals = 3
df = 8
size = 10**3
value_min = 0.5
value_max = 1.0
scale_number = 1
random_variable_type = 'normal' 
# options: normal student uniform exponential chi-squared


univar = random_variable_type 
if random_variable_type == 'normal':
    x = np.random.standard_t(df = df, size = size)
elif random_variable_type == 'student':
    x = np.random.standard_normal(df = df, size = size)
    univar = univar + ' df = ' + str(df)
elif random_variable_type == 'uniform':
    x = np.random.uniform(size = None)
    #x = np.random.uniform(low = value_min, high = value_max, size = None)
elif random_variable_type == 'exponential':
    x = np.random_variable_type(scale = scale_number, size = None)
    univar = univar + ' scale = ' + str(scale_number)
elif random_variable_type == 'chi_squared':
    x = np.random_variable_type(df = scale_number, size = size)
    univar = univar + ' df = ' + str(scale_number)
    
mu = np.mean(x)
sigma = np.std(x)
skew = skew(x)
kurt = kurtosis(x)
chi_func = chi2(x)

univar += '\n' + 'skewness= ' + str(np.round(skew, decimals)) + '\n' + 'kurtosis= ' + str(np.round(kurt, decimals)) + '\n' + 'mean= ' + str(np.round(mu, decimals)) + '\n' + 'volatility= ' + str(np.round(sigma, decimals))


plt.figure()
plt.hist(x, bins = 100)
plt.title(univar)
plt.show()