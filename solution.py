import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 170380561 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.04
    control_conversion = x_success / x_cnt
    test_conversion = y_success / y_cnt
    
    # Вычисляем комбинированную пропорцию
    combined_conversion = (x_success + y_success) / (x_cnt + y_cnt)
    
    # Вычисляем стандартную ошибку
    se = np.sqrt(combined_conversion * (1 - combined_conversion) * (1/x_cnt + 1/y_cnt))
    
    # Вычисляем Z-статистику
    z = (control_conversion - test_conversion) / se
    
    # Находим критическое значение Z-статистики
    critical_value = norm.ppf(1 - alpha/2) # двусторонний Z-тест
    
    # Принимаем решение на основе Z-статистики
    return abs(z) > critical_value
