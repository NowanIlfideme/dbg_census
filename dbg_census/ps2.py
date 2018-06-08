from dbg_census import census


class API(census.Stats):
	namespace = "ps2"

	def __str__(self):
		return "PLANETSIDE 2 STATS API"


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Character(Base):
    """Defines a PS2 character."""

    __tablename__ = 'character'

    character_id = Column(Integer, primary_key=True)
    faction_id = Column(Integer)
    name = Column(String) # Note - probably actually link to name.first

    def __repr__(self):
        return "<Character(character_id='%s', faction_id='%s')>" % (
                            self.character_id, self.faction_id)
    

class Outfit(Base):
    """Defines a PS2 outfit (clan)."""

    __tablename__ = 'outfit'

    outfit_id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    leader_character_id = Column(Integer, ForeignKey(Character.character_id))

    def __repr__(self):
        return "<Outfit(outfit_id='%s', alias='%s', name='%s')>" % (
                            self.outfit_id, self.alias, self.name)








