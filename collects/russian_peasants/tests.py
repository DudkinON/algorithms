from unittest import TestCase
from collects.russian_peasants import russian_peasants


class TestRussianPeasantsAlgorithm(TestCase):

    def test_russian_peasants(self):
        self.assertEquals(20, russian_peasants(4, 5))
        self.assertEquals(-20, russian_peasants(-4, 5))
        self.assertEquals(-20, russian_peasants(4, -5))
        self.assertEquals(20, russian_peasants(-4, -5))
        self.assertEquals(0, russian_peasants(0, 5))
        self.assertEquals(0, russian_peasants(4, 0))
