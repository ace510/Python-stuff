"""

# Column(Integer, Sequence('user_id_seq'), primary_key=True)


ed_user = User1(name='ed', fullname='Ed Jones', nickname='edsnickname')
# do this to create a new element of User1, attached to variable ed_user
# print(ed_user.nickname)
session.add(ed_user)
# add the new element to the session

session.commit()
our_user = session.query(User1).filter_by(name='ed').first()

# print(repr(our_user))

# if ed_user is our_user:
#    print('true')

session.add_all([
    User1(name='Ian', fullname='Ian Clark', nickname='Ace'),
    User1(name='Violet', fullname='Violet Love', nickname='Little Ratto'),
    User1(name='Dan', fullname='Dan Man', nickname='The') ])

print(session.dirty)

session.commit()

"""
