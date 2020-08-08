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
print ("Section at the end:", sec)
print ()

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

print ("Testing section cast methods")
print ("Adding to cast new member")
try:
    sess.add_member("Guy 1")
    print ("Guy 1 added")
    print (sess.get_cast())
except session.Cast_Error as error:
    print ("Guy 1 not added.", error)

print ("Adding to cast existing member")
try:
    sess.add_member("Guy 1")
    print ("Guy 1 added")
    print (sess.get_cast())
except session.Cast_Error as error:
    print ("Guy 1 not added.", error)

# bulk adds for testing
guy_number = 2
while guy_number <= 100:
    sess.add_member(f'Guy {guy_number}')
    guy_number += 1
print ("Cast after bulk adds:", sess.get_cast())

print ("Removing from cast existing member")
try:
    sess.remove_member("Guy 2")
    print ("Guy 2 removed")
except session.Cast_Error as error:
    print ("Guy 2 not removed.", error)

print ("Removing from cast non existant member")
try:
    sess.remove_member("Guy 2")
    print ("Guy 2 removed")
except session.Cast_Error as error:
    print ("Guy 2 not removed.", error)

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
