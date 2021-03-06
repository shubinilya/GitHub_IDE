import numpy as np

"""Игра угадай число
Компьютер сам загадывает и сам угадывает число методом последовательного приближения
"""

def approx_predict(number:int=1) -> int:
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
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток +
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(2) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    #print(random_array)

    for number in random_array:
        count_ls.append(approx_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    #print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
# score_game(random_predict)
if __name__ == '__main__':
    print(f'Ваш алгоритм угадывает число в среднем за: {score_game(approx_predict)} попыток')