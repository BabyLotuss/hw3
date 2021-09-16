from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
    jokes = []

    for _ in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)

        if flag:
            pass

        jokes.append(f'{noun} {adverb} {adjective}')

    return jokes


print(get_jokes(3))
