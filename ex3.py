ALPHABET = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЮЯ')


def thesaurus(item, *args):
    for idx in range(len(item)):
        some1 = filter(lambda el: el.startswith(item[idx]), args)
        print(f'{item[idx]}:', *some1)


thesaurus(ALPHABET, "Иван", "Мария", "Петр", "Екатерина", 'Ольга', 'Анастасия')
