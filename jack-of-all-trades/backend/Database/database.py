
from sqlalchemy import create_engine, CHAR, Column, String, Integer, ForeignKey, Boolean, BLOB
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    public_id = Column(String(60),unique=True, nullable=False, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    hashedPass = Column(String(60), unique=True, nullable=False)
    characters = relationship("character", backref="owner")

    def __init__(self, public_id, username, hashedPass):
        self.public_id = public_id
        self.username = username
        self.hashedPass = hashedPass

    def __repr__(self):
        return f"{self.public_id}"

class Character(Base):
    __tablename__ = "characters"

    char_id = Column(String(60), nullable=False, unique=True, primary_key=True)
    name = Column(String(30), nullable=False)  
    owned_by = Column(String(60), ForeignKey("users.public_id"), nullable=False)
    stats = relationship("statblock", backref="owner")
    inventory = relationship("inventory", backref="owner")
    statusFx = relationship("statusfx", backref="owner")
    skill_tree = relationship("skilltree", backref="owner")
    origin = relationship("origin", backref="owner")
    meta_data = relationship("metadata", backref="owner")

    def __init__(self, char_id, name, owned_by, stats, inventory, statusFx, skill_tree, origin, meta_data):
        self.char_id = char_id
        self.name = name
        self.owned_by = owned_by
        self.stats = stats
        self.inventory = inventory
        self.statusFx = statusFx
        self.skill_tree = skill_tree
        self.origin = origin
        self.meta_data = meta_data

    def __repr__(self):
        return f"({self.char_id}) called: {self.name}, owned by: {self.owned_by}"

class StatBlock(Base): 
    __tablename__ = "stats"

    stat_id = Column(String(60), ForeignKey("characters.char_id"), primary_key=True, nullable=False)
    health = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    armour = Column(Integer, nullable=False)
    evasion = Column(Integer, nullable=False)
    vim = Column(Integer, nullable=False)
    vigor = Column(Integer, nullable=False)
    charm = Column(Integer, nullable=False)
    wit = Column(Integer, nullable=False)
    attunement = Column(Integer, nullable=False)

    def __init__(self, stat_id, health, energy, armour, evasion, vim, vigor, charm, wit, attunement):
        self.stat_id = stat_id
        self.health = health
        self.energy = energy
        self.armour = armour
        self.evasion = evasion
        self.vim = vim
        self.vigor = vigor
        self.charm = charm
        self.wit = wit
        self.attunement = attunement

    def __repr__(self):
        return f"stats of character: {self.stat_id}"


class Inventory(Base):
    __tablename__ = "player_inventory"

    inventory_id = Column(String(60), ForeignKey("characters.char_id"), primary_key=True, nullable=False)
    max_weight = Column(Integer, nullable=False)
    current_weight = Column(Integer, nullable=False)
    items = relationship("itemcard", backref="owner")

class ItemCard(Base):
    __tablename__ = "item_card"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), nullable=False)
    item_id = Column(String(60), nullable=False, unique=True, primary_key=True)
    item_name = Column(String(40), nullable=False)
    item_img = Column(BLOB)
    item_type = Column(String(40), nullable=False)
    item_desc = Column(String(400))
    item_rarity = Column(Integer)
    max_dur = Column(Integer)
    current_dur = Column(Integer)
    stat_roll = Column(String(200))






Engine = create_engine(url="sqlite:///jack-of-all-trades/backend/Database/database.db", echo=True)
Base.metadata.create_all(bind=Engine)
        
Session = sessionmaker(bind=Engine)
session = Session()
