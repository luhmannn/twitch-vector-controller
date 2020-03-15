import anki_vector

class Vectorbot:

    def __init__(self):
        pass

    def say(self, message):
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            robot.behavior.say_text(message)