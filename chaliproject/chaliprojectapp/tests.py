from django.test import TestCase

import os
import django
if 'env setting':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YourRoot.settings')
    django.setup()
from django.test import TestCase
...

class SomeTest(TestCase):
    def test_one(self):  
        ...

    def test_two(self):
        ...
