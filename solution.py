import pandas as pd
import numpy as np


chat_id = 970839957 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    import scipy.stats as st
    alpha = 0.06
    t_statistic, p_value = st.ttest_1samp(x, 500, alternative="two-sided")
    return p_value < 2*alpha and x.mean() > 500
