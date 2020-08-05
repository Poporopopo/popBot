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
        if (not self.is_paused()):
            return
        section = section(self.cast, start_date)
        self.cast.append(section)
        return

    # closes the last section
    def stop_section(stop_date):
        # stops if:
        # previous section is still opened
        # no section exists
        if self.is_paused():
            return
        last_section = self.sections[-1]
        last_section.close(stop_date)

    # checks if the latest section is closed
    def is_paused():
        # returns true if no sections exist
        if (len(self.sections) < 1):
            return True
        last_section = self.sections[-1]
        return (not last_section.is_open())

class section:
    def __init__(self, cast, start_date):
        self.cast = cast.copy()
        self.start_date = start_date
        self.end_date = None

    def get_cast(self):
        return self.cast

    def get_start(self):
        return self.start_date

    def get_end(self):
        return self.end_date

    def set_end(self, end_date):
        self.end_date = end_date

    # checks if the section is closed
    def is_open(self):
        return self.get_end() == None

    # closes the section with a stop date
    def close(self, stop_date):
        if self.is_open():
            self.set_end(stop_date)
