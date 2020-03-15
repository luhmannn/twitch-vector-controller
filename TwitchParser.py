import re

class TwitchParser(object):

    def __init__(self):
        pass

    def parse(self, message):
        if (self.has_command(message)):
            return {
                'command': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(\![a-zA-Z0-9_]+) (.+)', message)[0]
            }

    def has_command(self, data):
        return re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(\![a-zA-Z0-9_]+) (.+)', data)
