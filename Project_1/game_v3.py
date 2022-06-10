"""Игра угадай число
Компьютер сам загадывает и сам угадывает число методом последовательного приближения
"""

import numpy as np


def approx_predict(number: int = 1) -> int:
    """Методом последовательного приближения угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100
    
    while True:
        count += 1
        
        predict_number = np.random.randint(min_number, max_number+1)  # произвольное предполагаемое число в диапазоне
        
        if number == predict_number:
            break  # выход из цикла если угадали
        else:
            # меняем диапазон поиска
            if predict_number < number:
                min_number = predict_number
            else:
                max_number = predict_number
    return count


def score_game(approx_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        approx_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(approx_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    print(count_ls)
    return score


if __name__ == "__main__":
    # RUN
    score_game(approx_predict)
