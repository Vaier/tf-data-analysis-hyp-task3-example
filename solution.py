import pandas as pd
import numpy as np
from scipy import stats


chat_id = 1251251937 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    stat, p_value = stats.ttest_ind(x, y, alternative='two-sided')
    return ( p_value < alpha)
