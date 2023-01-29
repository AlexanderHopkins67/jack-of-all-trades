from players_database import session, User

person = User("j649d", "Alex67", "bdasnjhd8w89uejwq")
# session.add(person)
# session.flush()
# print(session.new)
# session.commit
results = session.query(User).all()
print(results)