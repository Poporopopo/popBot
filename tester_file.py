from utl.classes import session_manager, session, section

print ("Testing section")
print ("Initializing section")
cast = ["guy 1", "guy 2"]
sec = section.section(cast, 2020)
print ("Section:", sec)
print ("Testing section methods")
print ("get_cast():", sec.get_cast())
print ("get_start():", sec.get_start())
print ("get_end():", sec.get_end())
print ("is_open():", sec.is_open())
print ("close(date):", sec.close(2021))
print ()

print ("Testing session")
print ("Initializing session")



# print ("Testing session manager")
#
# print("initializing session manager object")
# sm = session_manager()
# print (sm.sessions)
#
# print ("adding sessions")
# sm.open_session(20)
# sm.open_session(0)
# print (sm.sessions)
#
# print ("testing catch for duplicate session add")
# sm.open_session(20)
# print (sm.sessions)
#
# print ("removing sessions")
# sm.close_session(20)
# print (sm.sessions)
#
# print ("catch for removing nonexistant session")
# sm.close_session(20)
# print (sm.sessions)
