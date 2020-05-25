#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import numpy as np

def game_core(number):
    count = 1
    low = 1
    up = 101
    predict = 50

    while number != predict:
        if predict > number: 
            up = predict
        elif predict < number: 
            low = predict

        predict = int((low+up)/2)
        count += 1
    return(count) # выход из цикла, если угадали

        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return(score)


score_game(game_core)


# In[ ]:




