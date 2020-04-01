import anki_vector
import time
from anki_vector.util import degrees
from anki_vector import behavior

class VectorPosition():

    def __init__(self):
        pass

    def perform(self, parameter):
        args = anki_vector.util.parse_command_args()

        with anki_vector.Robot(args.serial) as robot:

            try:
                robot.behavior.drive_on_charger()

                time.sleep(10)

                robot.behavior.drive_off_charger()

                time.sleep(10)

                degr = 360

                robot.behavior.say_text("now i will begin turning %s degrees" % degr)

                robot.behavior.turn_in_place(degrees(360), is_absolute=1, num_retries=3)

                time.sleep(10)

                robot.behavior.say_text("i have finished turning")
            except Exception as err:
                print(err)

            