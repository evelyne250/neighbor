from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.eve = Profile( user = 'eve', profile_picture  = '/', bio = 'my tests', contact='uevelyne44@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.eve,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.eve.save_profile()
        eve = Profile.objects.all()
        self.assertTrue(len(eve) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
       