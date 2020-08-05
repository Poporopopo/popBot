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
        # if the previous section is still open, will not make a new one
        if (not is_paused()):
            return
        section = section(self.cast, start_date)
        self.cast.append(section)
        return

    # checks if the latest section is closed
    def is_paused():
        if (len(self.cast) < 1):
            return True
        last_section = self.cast[-1]
        return (not last_section.is_open())

class section:
    def __init__(self, cast, start_date):
        self.cast = cast.copy()
        self.start_date = start_date
        self.end_date = None

    def is_open():
        return self.end_date == None
