from utl.exceptions.session_exceptions import *
from utl.classes.session import *

# initializing session manager object
sm = session_manager()
print (sm.sessions)

# adding sessions
sm.open_session(20)
sm.open_session(0)
print (sm.sessions)

# testing catch for duplicate session add
sm.open_session(20)
print (sm.sessions)

# removing sessions
sm.close_session(20)
print (sm.sessions)

# catch for removing nonexistant session
sm.close_session(20)
print (sm.sessions)
