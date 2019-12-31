import datetime

from django.test import TestCase
from .models import Feature


class FeatureModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        Silly test to check if name is set correctly
        """
        name = 'some_name'
        feature = Feature(name=name)
        self.assertIs(name, feature.name)