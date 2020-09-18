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
            self.sessions.remove(to_remove)
        except Session_Error as error:
            raise error

    # checks if session is open
    # if is tries to add member to cast
    def add_member(self, id, name):
        try:
            session_to_update = self.get_session(id)
        except Session_Error as error:
            raise error
        else:
            session_to_update.add_member(name)

    # checks if session is opens
    # if open, tries to remove member from cast
    def remove_member(self, id, name):
        try:
            session_to_update = self.get_session(id)
        except Session_Error as error:
            raise error
        else:
            session_to_update.remove_member(name)

    # given a valid id, tells corresponding session to create a section
    def session_create_section(self, id, start_message, end_message):
        try:
            session_to_update = self.get_session(id)
        except Session_Error as error:
            print (error)
        else:
            session_to_update.create_section(start_message, end_message)

    # checks if session exists, else throws error
    # asks session to start a section
    def start_in_session(self, id, date):
        try:
            sess = self.get_session(id)
        except Session_Error as error:
            raise error
        except session.Pause_Error as error:
            raise error
        else:
            sess.start_section(date)

    # checks if session exists, else throws error
    # asks session to close a section
    def close_in_session(self, id, date):
        try:
            sess = self.get_session(id)
        except Session_Error as error:
            raise error
        except session.Pause_Error as error:
            raise error
        else:
            sess.stop_section(date)

class Session_Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))
