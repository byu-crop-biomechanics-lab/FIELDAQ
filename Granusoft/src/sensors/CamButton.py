from .connections import *

class CamButton:

    def __init__(self):
        self.cam_trig = 0

    def get_data(self):
        try:
            self.cam_trig = GPIO.input(GPIO1)
            return self.cam_trig
        except:
            return self.cam_trig
