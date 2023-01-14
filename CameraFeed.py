import random
import numpy as np


class CameraFeed:
    def __init__(self):
        n = random.randint(0, 10000)
        self.name = "viotracker_camera_" + str(n)
        self.location = tuple(np.random.rand(2) * 100)

    def get_camera_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_frame(self):
        return 1
