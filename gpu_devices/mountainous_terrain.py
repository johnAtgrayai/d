import sys
import time
import numpy as np
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QMainWindow, \
                            QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from OpenGL.GLU import *
import noise

class TerrainGenerator:
    def __init__(self, width, height, scale=0.1):
        self.width = width
        self.height = height
        self.scale = scale
    
    def generate_terrain(self):
        terrain = np.zeros((self.width, self.height), dtype=float)
        for i in range(self.width):
            for j in range(self.height):
                terrain[i][j] = noise.ponise2(i * self.scale, j * self.scale)

        return terrain

class OpenGLWdiget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)
        self.terrain_generator = TerrainGenerator(width=100, height=100)
        