# pylint: disable=missing-docstring
import unittest

from ballgame.vector import Vector


class VectorTest(unittest.TestCase):

    def test_sum(self):
        vec1 = Vector(3, 6)
        vec2 = Vector(-4, 1)
        result = Vector(-1, 7)
        self.assertEqual(vec1 + vec2, result)
