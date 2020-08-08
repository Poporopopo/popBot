from utl.classes import session_manager, session, section

# Section testing
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
print ("Section at the end:", sec)
print ()

# session testing
print ("Testing session")
print ("Initializing session")
sess = session.session(22222)
print ("Initialized session:", sess)
print ()
print ("Testing section methods get methods")
print ("get_id():", sess.get_id())
print ("get_cast():", sess.get_cast())
print ("get_sections:", sess.get_sections())
print ()

# session testing: cast methods
print ("Testing section cast methods")
print ("Adding to cast new member")
try:
    sess.add_member("Guy 1")
    print ("Guy 1 added")
except session.Cast_Error as error:
    print ("Guy 1 not added.", error)
print()

print ("Adding to cast existing member")
try:
    sess.add_member("Guy 1")
    print ("Guy 1 added")
except session.Cast_Error as error:
    print ("Guy 1 not added.", error)
print()

# bulk adds for testing
guy_number = 2
while guy_number <= 100:
    sess.add_member(f'Guy {guy_number}')
    guy_number += 1
del guy_number
print ("Cast after bulk adds:", sess.get_cast())
print()

print ("Removing from cast existing member")
try:
    sess.remove_member("Guy 2")
    print ("Guy 2 removed")
except session.Cast_Error as error:
    print ("Guy 2 not removed.", error)
print()

print ("Removing from cast non existant member")
try:
    sess.remove_member("Guy 2")
    print ("Guy 2 removed")
except session.Cast_Error as error:
    print ("Guy 2 not removed.", error)
print()

# session testing: section creation
print ("Testing start_section()")
sess.cast = []
print ("Start a section with empty cast")
try:
    sess.start_section(2020)
    print ("Section added")
except session.Pause_Error as error:
    print (error)
except session.Cast_Error as error:
    print (error)
print()

guy_number = 1
while guy_number <= 100:
    sess.add_member(f'Guy {guy_number}')
    guy_number += 1
del guy_number

print ("Starting a section with a cast")
try:
    sess.start_section(2020)
    print ("Section added")
except session.Pause_Error as error:
    print (error)
except session.Cast_Error as error:
    print (error)
print ()

print ("Starting a section with one already started")
try:
    sess.start_section(2020)
    print ("Section added")
except session.Pause_Error as error:
    print (error)
except session.Cast_Error as error:
    print (error)
print()

# session testing: section closing
print ("Closing section when one is started")
try:
    sess.stop_section(2021)
    print ("Section closed")
except session.Pause_Error as error:
    print (error)
print ()

print ("Closing a section when none is started")
try:
    sess.stop_section(2021)
    print ("Section closed")
except session.Pause_Error as error:
    print (error)
print ()

# section_manager testing
print ("Testing session manager")
print("Initializing session manager object")
sm = session_manager.session_manager()
print ("Initialized session_manager", sm)
print ()

# adding session testing
print ("adding sessions")
sm.open_session(20)
sm.open_session(0)
print (sm)
print ()

print ("testing catch for duplicate session add")
try:
    sm.open_session(20)
except session_manager.Session_Error as error:
    print ("session has not been opened")
    print (error)
print (sm)
print ()

# removing section testing
print ("removing sessions")
sm.close_session(20)
print (sm)
print ()

print ("testing catch for removing nonexistant session")
try:
    sm.close_session(20)
except session_manager.Session_Error as error:
    print (error)
print (sm)
print ()
