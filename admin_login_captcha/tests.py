"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse,  NoReverseMatch
from django.core.exceptions import ImproperlyConfigured


class CaptchaTest(TestCase):
    def test_captcha_image(self):
        """
        Tests that captcha images can be successfully reached.
        """
        try:
            image_url = reverse('captcha-image', args=('dummy',))
        except NoReverseMatch,e:
            raise ImproperlyConfigured('Make sure you\'ve included captcha.urls as explained in the INSTALLATION section on http://code.google.com/p/django-simple-captcha/')

