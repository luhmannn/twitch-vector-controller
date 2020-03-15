import anki_vector
from PIL import Image
import os
import time

class VectorBananas():

    def __init__(self):
        pass

    def perform(self, duration):
        args = anki_vector.util.parse_command_args()

        with anki_vector.Robot(args.serial) as robot:
            dir = os.path.dirname(__file__)
            filename = os.path.join(dir, 'assets', 'bananas.jpg')

            image_file = Image.open(filename)

            int_duration = int(duration)

            if (image_file):
                print("got file")
                screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
                robot.screen.set_screen_with_image_data(screen_data, int_duration)
                time.sleep(int_duration)    
