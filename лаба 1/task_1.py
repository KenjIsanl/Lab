import doctest


class Fridge:
    def __init__(self, is_open: bool, capacity_volume, occupied_volume: int):
        """
        Создание и подготовка к работе объекта "Холодильник"

        :param capacity_volume: Объем холодильника
        :param occupied_volume: Объем еды в холодильнике

        Примеры:
        >>> fridge = Fridge(True, 500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, int):
            raise TypeError("Объем холодоса должен быть типа int")
        if capacity_volume <= 0:
            raise ValueError("Объем холодоса должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, int):
            raise TypeError("Количество еды должно быть int")
        if occupied_volume < 0:
            raise ValueError("Количество еды не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

        self.is_open = is_open

    def is_fridge_open(self) -> bool:
        """
        Функция которая проверяет является ли является холодильник открытым

        :return: Является ли открытым холодильник

        Примеры:
        >>> fridge = Fridge(True, 500, 0)
        >>> fridge.is_fridge_open()
        True
        """
        return self.is_open

    def add_food_to_fridge(self, food: int) -> None:
        """
        Добавляем еду в холодос.
        :param food: Количество еды, которую добавляем в холодос

        :raise ValueError: Если еда не помощается в холодос, не является целым числом и не является положительным.


        Примеры:
        >>> fridge = Fridge(True, 500, 0)
        >>> fridge.add_food_to_fridge(155)
        """
        if not isinstance(food, int):
            raise TypeError("Добавляемая еда должна быть типа int")
        if food < 0:
            raise ValueError("Добавляемая еда должна положительным числом")
        if self.capacity_volume > food + self.occupied_volume:
            self.capacity_volume += food
        else:
            raise ValueError("Нет места в холодосе")


class Bed:
    def __init__(self, is_bed_made_up, is_bed_comfortable: bool, number_of_pillows: int):
        """
        Создание и подготовка к работе объекта "Кровать"

        :param number_of_pillows: Количество игрушек
        :param is_bed_made_up: Заправлена ли кровать
        :param is_bed_comfortable: Комфортна ли кровать

        Примеры:
        >>> bed = Bed(False, True, 1)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_pillows, int):
            raise TypeError("Количество подушек должно быть класса int")
        if number_of_pillows <= 0:
            raise ValueError("Количество подушек должно быть положительным числом")
        self.number_of_pillows = number_of_pillows
        self.is_bed_made_up = is_bed_made_up
        self.is_bed_comfortable = is_bed_comfortable

    def is_my_bed_made_up(self) -> bool:
        """
        Функция которая проверяет заправлена ли моя кровать

        :return: Является ли моя кровать заправленной

        Примеры:
        >>> bed = Bed(True, True, 1)
        >>> bed.is_my_bed_made_up()
        True
        """
        return self.is_bed_made_up

    def add_pillows_on_bed(self, pillows: int) -> None:
        """
        Добавляем подушки на кровать.
        :param pillows: Подушки, которые я добавляю на кровать


        Примеры:
        >>> bed = Bed(False, True, 1)
        >>> bed.add_pillows_on_bed(2)
        >>> print(bed.number_of_pillows)
        3
        """
        if not isinstance(pillows, int):
            raise TypeError("Добавляемые подушки должны быть типа int")
        if pillows < 0:
            raise ValueError("Добавляемые подушки должны быть положительными")
        self.number_of_pillows += pillows

    def is_my_bed_comfortable(self) -> bool:
        """
        Функция которая проверяет комфортна ли моя кровать

        :return: Является ли моя кровать комфортной

        Примеры:
        >>> bed = Bed(False, True, 1)
        >>> bed.is_my_bed_comfortable()
        False
        """
        if self.number_of_pillows >= 3:
            self.is_bed_comfortable = True
        else:
            self.is_bed_comfortable = False

        return self.is_bed_comfortable


class Game:
    def __init__(self, is_open_game: bool, total_score: float, death_counter: int):
        """
        Создание и подготовка к работе объекта "Игра"

        :param is_open_game: Открыта ли игра
        :param death_counter: Количество смертей
        :param total_score: Конечное количество очков

        Примеры:
        >>> game = Game(True, 500.5, 3)  # инициализация экземпляра класса
        """
        if not isinstance(total_score, (int, float)):
            raise TypeError("Количество очков должно быть класса int или float")
        if total_score < 0:
            raise ValueError("Количество очков должно быть положительным числом")
        self.is_open_game = is_open_game
        self.total_score = total_score
        self.death_counter = death_counter

    def do_i_won(self) -> bool:
        """
        Функция которая проверяет выиграл ли я

        :return: Является ли игра выигрышной

        Примеры:
        >>> game = Game(True, 545.5, 4)
        >>> game.do_i_won()
        True
        """
        if self.total_score > 400 and self.death_counter < 10:
            is_won = True
        else:
            is_won = False
        return is_won

    def close_my_game(self) -> None:
        """
        Закрытие игры


        Примеры:
        >>> game = Game(True, 500, 3)
        """
        if self.is_open_game is True:
            self.is_open_game = False
        else:
            raise ValueError("Игра итак закрыта")


if __name__ == "__main__":
    doctest.testmod()
