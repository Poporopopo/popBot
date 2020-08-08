from utl.classes import session

class session_manager:
    def __init__(self, sessions=[]):
        self.sessions = sessions.copy()

    def __str__(self):
        output = []
        for session in self.sessions:
            output.append(session.__str__())
        return str(output)

    def get_session(self, id):
        for a_session in self.sessions:
            if a_session.get_id() == id:
                return a_session
        # if not matching is found
        raise Session_Error("Session does not exist")

    # boolean check for exising session
    def is_session_open(self, id):
        for a_session in self.sessions:
            if a_session.get_id() == id:
                return True
        return False

    # boolean check for session is paused
    # throws error if session does not exist
    def is_session_paused(self, id):
        try:
            to_check = self.get_session(id)
            return to_check.is_paused()
        except Session_Error as error:
            raise error

    # opens a session if it doesn't exist
    def open_session(self, id):
        if self.is_session_open(id):
            raise Session_Error("Session already exists")
        self.sessions.append(session.session(id))

    # closes a session if it exists
    def close_session(self, id):
        # searches for session
        try:
            to_remove = self.get_session(id)
            # TODO: close and save the session beforehand
            self.sessions.remove(to_remove)
        except Session_Error as error:
            raise error

    # checks if session is open
    # if is tries to add member to cast
    def add_member(self, id, name):
        try:
            to_add = self.get_session(id)
        except Session_Error as error:
            raise error
        else:
            try:
                to_add.add_member(name)
            except session.Cast_Error as error:
                raise error

    # checks if session is opens
    # if open, tries to remove member from cast
    def remove_member(self, id, name):
        try:
            to_remove = self.get_session(id)
        except Session_Error as error:
            raise error
        else:
            try:
                to_remove.remove_member(name)
            except session.Cast_Error as error:
                raise error

class Session_Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))
