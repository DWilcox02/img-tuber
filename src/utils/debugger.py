
class Debugger:

    def __init__(self, debug=False):
        self.should_debug = debug

    def debug(self, msg, override):
        if override or self.should_debug:
            print(msg)