from coordinate import Coordinate


class Cell:
    """Cell - superclass for all kinds of cells that are in the ocean"""

    def __init__(self, settings):
        # self.offset = offset
        self.image = settings.image_for_cell
        # self.x = coordinate.x
        # self.y = coordinate.y

    def __repr__(self):
        return self.image

    def get_off_set(self):
        """Возвращает смещение"""
        pass

    def set_off_set(self, a_coord):
        """Устанавливает смещение в a_coord"""
        pass

    def get_image(self):
        """return image"""
        pass

    def display(self):
        """Выводит изображение по соответствующему смещению"""
        pass

    def process(self):
        """Перемещает в соседнюю ячейку, используя определенные правила (в зависимости от подкласса)"""
        pass

    def get_empty_neighbor_coord(self):
        """Ищет соседнюю пустую ячейку"""
        pass

    def get_prey_neighbor_coord(self):
        """Ищет соседнюю ячейку с добычей"""
        pass

    def get_cell_at(self, a_coord):
        """Возвращает ячейку с координатами a_coord в массиве cells из ocean"""
        pass

    def assign_cell_at(self, a_coord, a_cell):
        """Помещает ячейку a_cell в место с координатоми a_coord в массиве cells"""
        pass

    def east(self):
        """Возвращает ячейку, на востоке от данной"""
        pass

    def north(self):
        """Возвращает ячейку, на севере от данной"""
        pass

    def south(self):
        """Возвращает ячейку, на юге от данной"""
        pass

    def west(self):
        """Возвращает ячейку, на западе от данной"""
        pass
