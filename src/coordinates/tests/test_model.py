from django.test import TestCase

from coordinates.models import Coordinate


class TestCoordinate(TestCase):

    @classmethod
    def setUpTestData(cls):
        Coordinate.objects.create(11.111111, 11.111111)
        pass

