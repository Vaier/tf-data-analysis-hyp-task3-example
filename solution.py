import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import mannwhitneyu

chat_id = 1251251937 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.09
    
    pval = stats.ttest_ind(x, y).pvalue
    if pval < alpha:
      res = True
    else:
      res = False    
    return res 
