class Session_Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

class Cast_Error(Exception):
    def __init__ (self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

class Pause_Error(Exception):
    def __init__ (self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))
