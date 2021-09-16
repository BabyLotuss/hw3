def num_translate(eng):
    nums = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    return nums.get(eng)


print(num_translate(input('Введите натуральное число от 1 до 10 на английском: ')))
