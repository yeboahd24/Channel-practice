from django.urls import path
from . views import *

path('', counting, name='counting'),