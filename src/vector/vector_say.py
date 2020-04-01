import anki_vector

class VectorSay:

    def __init__(self):
        pass

    async def perform(self, message):
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            robot.behavior.say_text(message)