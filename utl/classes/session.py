from utl.exceptions.session_exceptions import *

class session_manager:
    def __init__(self, sessions=[]):
        self.sessions = sessions.copy()

    def get_session(self, id):
        for session in self.sessions:
            if session.get_id() == id:
                return session
        # if not matching is found
        raise Session_Error("Session does not exist")

    # # private method, don't use
    # def remove_session(self, id):
    #     # searches for session
    #     to_remove = self.get_session(id)
    #     # TODO: close and save the session beforehand
    #     self.sessions.remove(to_remove)

    # opens a session if it doesn't exist
    def open_session(self, id):
        try:
            get_session(id)
        except Session_Error:
            self.sessions.append(session(id))

    # closes a session if it exists
    def close_session(self, id):
        # searches for session
        try:
            to_remove = self.get_session(id)
            # TODO: close and save the session beforehand
            self.sessions.remove(to_remove)
        except Session_Error as error:
            error

    def is_session_paused(self, id):
        if self.session_exists(id):
            return
        return

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

class section:
    def __init__(self, cast, start_date):
        self.cast = cast.copy()
        self.start_date = start_date
        self.end_date = None

    def get_cast(self):
        return self.cast.copy()

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
