import pygame
from entity import *
from constants import *

class FinishFlag(Entity):
    containers = ()
    
    def __init__(self, x, y):
        super().__init__(self, x, y)

