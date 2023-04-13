import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 317456038 #Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: #Одна или две выборке на входе, заполняется исходя из условия
    #Измените код этой функции
    #Это будет вашим решением
    #Не меняйте название функции и её аргументы
    return stats.ttest_ind(x, y)[1] < 0.09
