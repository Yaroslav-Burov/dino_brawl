from unittest import TestCase

from Game import calc
from Game import jump
from Game import dino_jump_height
from Game import dino_y


class Test(TestCase):
    def test_calc(self):
        self.assertEqual(calc(4, 5), 9)

    def test_jump(self):
        dino_jump_height = -12
        jump()
        self.assertEqual(dino_y, 800)

