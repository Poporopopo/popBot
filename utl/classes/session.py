class Session:
    def __init__(self, id ,cast=[], sections=[]):
        self.id = id
        self.cast = cast
        self.sections = sections

    # takes name <string> add pushes to cast array
    def add_member(name):
        self.cast.push(name)

    # takes name <string> and removes from cast array
    def remove_member(name):
        self.cast.remove(name)

    # creates a new section
    def start_section(start_date):
        
        return


def Section:
    def __init__(self, cast, start_date):
        self.cast = cast.copy()
        self.start_date = start_date
        self.end_date = None

    def is_open():
        return self.end_date == None
