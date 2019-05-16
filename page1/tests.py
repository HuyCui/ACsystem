from django.test import TestCase
from django.http import request
# Create your tests here.

action = request.COOKIES('actionid')
print(action)
