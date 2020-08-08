class session_manager:
    def __init__(self, sessions=[]):
        self.sessions = sessions.copy()

    def get_session(self, id):
        for session in self.sessions:
            if session.get_id() == id:
                return session
        # if not matching is found
        raise Session_Error("Session does not exist")

    # opens a session if it doesn't exist
    def open_session(self, id):
        try:
            self.get_session(id)
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
            raise error

    def is_session_paused(self, id):

        return

class Session_Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))
