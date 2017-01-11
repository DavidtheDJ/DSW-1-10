#David Justice
#12-14-16
#sheep pixmap

from graphic_animal_item_class import *
from sheep_class import *

import field_resources

class SheepGraphicsPixmap(AnimalGraphicsPixmapItem):
    """this class provides a graphical represantation of a sheep"""

    #constructor
    def __init__(self):
        self.available_graphics = [":/sheep_baby.png", ":/sheep_poor.png",
                                   ":/sheep_fine.png", ":/sheep_prime.png"]

        super().__init__(self.available_graphics)

        self.animal = sheep("")
