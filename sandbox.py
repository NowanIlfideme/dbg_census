
from dbg_census.ps2 import API

api = API()

# get all available collections
api.collections()

# check a specific collection
api.collection('character')


# just an example
fcrw = api("outfit", {"alias":"FCRW", "c:resolve":"member_online_status,member_character(name)"})
members = fcrw["outfit_list"][0]["members"]
member_ids = map(lambda x: x['character_id'], members)
list(member_ids)



from sqlalchemy import create_engine
from dbg_census.ps2 import Base

# Finished defining - we make
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)


from dbg_census.ps2 import Character, Outfit

# Sandbox place
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

# Example
me = Character(character_id=666, faction_id=1337)
session.add(me)
leetfit = Outfit(
     leader_character_id=me.character_id, 
     name="leetfit", alias="1337")
session.add(leetfit)

session.commit()

for dude in session.query(Character):
    print(dude)

for fit in session.query(Outfit):
    print(fit)
