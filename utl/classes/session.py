from utl.classes import section

class session:
    def __init__(self, id ,cast=[], sections=[]):
        self.id = id
        self.cast = cast.copy()
        self.sections = sections.copy()

    def __str__(self):
        sections = []
        for section in self.sections:
            sections.append(section.__str__())
        output = {
            "ID" : self.id,
            "cast" : self.cast,
            "sections": sections
        }
        return str(output)

    def get_id(self):
        return self.id

    def get_cast(self):
        return self.cast.copy()

    def get_sections(self):
        return self.sections.copy()

    def is_in_cast(self, name):
        return name in self.get_cast()

    # takes name <string> add pushes to cast array
    def add_member(self, name):
        if not self.is_in_cast(name):
            self.cast.append(name)

    # takes name <string> and removes from cast array
    def remove_member(self, name):
        if self.is_in_cast(name):
            self.cast.remove(name)

    def create_section(self, start_message, end_message):
        new_section = section.section(self.cast, start_message, end_message)
        self.sections.append(new_section)
        return

    def update_last_section_cast(self):
        last_section = self.sections[-1]
        last_section.update_cast(cast)

# class Cast_Error(Exception):
#     def __init__ (self, value):
#         self.value = value
#
#     def __str__(self):
#         return (repr(self.value))
#
# class Pause_Error(Exception):
#     def __init__ (self, value):
#         self.value = value
#
#     def __str__(self):
#         return (repr(self.value))
