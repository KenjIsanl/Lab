# TODO: описать базовый класс


class Network:
    """Класс сеть"""
    def __init__(self, name: str, year: int, is_working: bool):
        """
        Создание объекта "Сеть"

        :param name: название сети
        :param year: год создания сети
        :param is_work: статус включена/выключена ли сеть

        """
        self._name = name
        self._year = year
        self.is_working = is_working

    def turn_on(self):
        """Функция, которая включает сеть, если она выключена"""
        if self.is_working is False:
            self.is_working = True

    @property
    def name(self) -> str:
        """Возвращает название в виде строки"""
        return self._name

    @property
    def year(self) -> int:
        """Возвращает год в виде int"""
        return self._year

    def __str__(self):
        """Магический-метод, который выводит результат экземпляра (для чтения)"""
        return f"Социальная сеть: {self.name}. Год создания: {self.year}. Работает? {self.is_working}"

    def __repr__(self):
        """Магический метод, который тоже выводит"""
        return f"{self.__class__.__name__}(name={self.name!r}, year={self.year!r})"


social = Network('Vk', 1999, False)
social.turn_on()
print(f"{social}")
print(repr(social))  # Проверка экземпляром: работа метода,и repr.

# TODO: описать дочерний класс


class Youtube(Network):
    """Класс Ютуб"""
    def __init__(self, name: str, year: int, is_working: bool, video: str, video_duration: int):
        """
        Создание объекта "Сеть"

        :param name: название
        :param year: год создания
        :param is_working: статус включен/выключен
        :param video: какое видео включено
        :param video_duration: сколько минут видео длиться
        """
        super().__init__(name, year, is_work)
        """Наследование param: name, year, is_work от класса Network"""
        self.video = video
        self._video_duration = video_duration

    @property
    def video_duration(self) -> float:
        """Вовращает длительность видео в виде float"""
        return self._video_duration

    @video_duration.setter
    def video_duration(self, value):
        """Устанавливает длительность ролика"""
        if not isinstance(value, float):
            raise TypeError("Продолжительность должна быть типа float")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._video_duration = value

    def is_yt_working(self) -> bool:
        return self.is_working

    def __str__(self):
        return f"Социальная сеть: {self.name}. Год создания: {self.year}. Работает? {self.is_working}. " \
               f"Ролик: {self.video}. Продолжительность (минуты): {self._video_duration}"


pr1 = Youtube('YouTube', 2005, False, 'Как нестандартно мыслить', 666)  # Просто экземлпяр
pr1.turn_on()
print(pr1)
