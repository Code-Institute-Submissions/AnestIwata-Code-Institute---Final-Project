from django.test import TestCase
from accounts.models import Profile, get_user_model


#
# user = models.OneToOneField(User, on_delete=models.CASCADE)
#     donations = models.FloatField(default=0)
#     name = models.CharField(max_length=100, blank=True)
#     surname = models.CharField(max_length=100, blank=True)
#     email = models.CharField(max_length=100, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

class ProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create()

    def test_profile(self):
        profile = get_user_model().objects.last().profile
