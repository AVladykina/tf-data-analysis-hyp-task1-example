import pandas as pd
import numpy as np
import math
from scipy.stats import norm

chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    alpha=0.05
    p_control = x_success / x_cnt
    p_test = y_success / y_cnt
    p_pool = (x_success + y_success) / (x_cnt + y_cnt)

    se_diff = math.sqrt(p_pool * (1 - p_pool) * (1/x_cnt + 1/y_cnt))
    z_score = (p_test - p_control) / se_diff

    p_value = 2 * (1 - norm.cdf(abs(z_score)))
    return p_value < alpha
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
     # Ваш ответ, True или False
