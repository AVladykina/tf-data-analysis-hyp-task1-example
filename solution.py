import pandas as pd
import numpy as np
import math
from scipy.stats import norm
from statsmodels.stats.proportion import proportion_confint

chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    conv_control = x_success / x_cnt

    # Доля конверсии в тестовой группе
    conv_test = y_success / y_cnt

    # Разница долей конверсии
    diff = conv_test - conv_control

    # Доверительный интервал на разность долей конверсии
    ci_low, ci_high = proportion_confint(count=[y_success, x_success], nobs=[y_cnt, x_cnt], alpha=0.05, method='wilson')

    # Проверяем, содержит ли доверительный интервал ноль
    return  ci_low.any() < 0
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
     # Ваш ответ, True или False
