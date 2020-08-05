class session:
    def __init__(self, id ,cast=[], sections=[]):
        self.id = id
        self.cast = cast.copy
        self.sections = sections.copy

    # takes name <string> add pushes to cast array
    def add_member(name):
        self.cast.push(name)

    # takes name <string> and removes from cast array
    def remove_member(name):
        self.cast.remove(name)

    # creates a new section
    def start_section(start_date):
        section = section(cast, start_date)
        self.cast.append(section)
        return

def section:
    def __init__(self, cast, start_date):
        self.cast = cast.copy()
        self.start_date = start_date
        self.end_date = None

    def is_open():
        return self.end_date == None
