class session:
    def __init__(self, id ,cast=[], sections=[]):
        self.id = id
        self.cast = cast.copy()
        self.sections = sections.copy()

    def get_id(self):
        return self.id

    def get_cast(self):
        return self.cast.copy()

    def get_sections(self):
        return self.sections.copy()

    # takes name <string> add pushes to cast array
    def add_member(self, name):
        if name in self.get_cast():
            raise (Cast_Error("Member already added"))
        else:
            self.cast.append(name)

    # takes name <string> and removes from cast array
    def remove_member(self, name):
        if name in self.get_cast():
            self.cast.remove(name)
        else:
            raise (Cast_Error("Member not in Cast"))

    # creates a new section
    def start_section(self, start_date):
        # if the previous section is still open, will not make a new one
        if (not self.is_paused()):
            raise (Pause_Error("A section is already open"))
        new_section = section(self.cast, start_date)
        self.sections.append(new_section)
        return

    # closes the last section
    def stop_section(self, stop_date):
        # stops if:
        # previous section is still opened
        # no section exists
        if self.is_paused():
            raise (Pause_Error("No sections to close"))
        last_section = self.sections[-1]
        last_section.close(stop_date)

    # checks if the latest section is closed
    def is_paused(self):
        # returns true if no sections exist
        if (len(self.sections) < 1):
            return True
        last_section = self.sections[-1]
        return (not last_section.is_open())

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
