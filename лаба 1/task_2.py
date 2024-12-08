from task_1 import Book,Games,Computer  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    book = Book('LD','Romance')
    game = Games('Dota 2', 0)
    computer = Computer('ASUS TUF', 'Asus')

 # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        book._genre_valid("Detective")
     # TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        game._title_valid("Assasin Creed")
     # TODO: вызвать метод с некорректными аргументами(a)
    except Error:
        print('Ошибка: неправильные данные')

    try:

        computer._model_valid("Acer")
    # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')
