from prey import Prey


class Predator(Prey):
    """Subclass Prey, predator, can move, breed, eat prey"""

    def __init__(self, ocean, settings, x=0, y=0):
        super().__init__(ocean,settings)
        self.settings = settings
        self.time_to_feed = 6
        self.image = settings.image_for_predator
        self.number_of_element = settings.predators_number

        self.x = x
        self.y = y

    def __repr__(self):
        return self.settings.image_for_predator

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""
        # print(f'procwss for predator {self.x, self.y}')
        pass

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass
