from task_1 import Fridge, Bed, Game

if __name__ == "__main__":
    fridge = Fridge(True, 700, 4)
    bed = Bed(False, False, 1)
    game = Game(False, 268.38, 1)

    try:
        fridge.add_food_to_fridge(-5)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        bed.add_pillows_on_bed(-5)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        game.close_my_game()
    except ValueError:
        print('Ошибка: неправильные данные')

