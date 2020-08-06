from utl.exceptions.session_exceptions import *
from utl.classes.session import *

# initializing session manager object
sm = session_manager()
print (sm.get_sessions())

# adding sessions
sm.open_session(20)
sm.open_session(0)
print (sm.get_sessions())

# testing catch for duplicate session add
sm.open_session(20)
print (sm.get_sessions())

# removing sessions
sm.remove_session(20)
print (sm.get_sessions())

# catch for removing nonexistant session
sm.remove_session(20)
print (sm.get_sessions())
