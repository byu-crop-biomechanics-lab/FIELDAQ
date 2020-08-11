"""
This screen needs to accept information about which image to view. Then display
that image. The image can be deleted via this screen [not sure if this
feature should be kept or not], or the user can return to the ImagesViewScreen.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from view.BaseScreen import BaseScreen
from Sensor import Sensor
import datetime

import os

try:
    from PIL import Image as pili
except ImportError:
    print("Failed to import Pillow Library")
    import pip
    pip.main(['install', '--user', 'Pillow'])
    os.system('sudo reboot')

Builder.load_file('view/screens/camera/ImageReviewScreen.kv')

class ImageReviewScreen(BaseScreen):
    image_name = StringProperty()

    def set_image(self, name):
        self.image_name = name
        self.image_path = "Images/" + name

    def delete_button(self):
        print('We should delete image ' + self.image_name)
        #os.system("rm " + self.image_path)
