
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
    campaigns = relationship("campaign", backref="owner")

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
    affiliation = relationship("affiliation", backref="owner")
    statusFx = relationship("statusfx", backref="owner")
    perks = relationship("perk", backref="owner")
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
    __tablename__ = "stat_blocks"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), primary_key=True, nullable=False)
    health = Column(Integer, nullable=False)
    max_health = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    max_energy = Column(Integer, nullable=False)
    exhaustion = Column(Integer, nullable=False)
    armour = Column(Integer, nullable=False)
    evasion = Column(Integer, nullable=False)
    vim = Column(Integer, nullable=False)
    vigor = Column(Integer, nullable=False)
    charm = Column(Integer, nullable=False)
    wit = Column(Integer, nullable=False)
    attunement = Column(Integer, nullable=False)

    def __init__(self, owner_id,
        stat_id, health, max_health, energy, max_energy, exhaustion, armour,
        evasion, vim, vigor, charm, wit, attunement
        ):
        self.owner_id = owner_id
        self.stat_id = stat_id
        self.health = health
        self.max_health = max_health
        self.energy = energy
        self.max_energy = max_energy
        self.exhaustion - exhaustion
        self.armour = armour
        self.evasion = evasion
        self.vim = vim
        self.vigor = vigor
        self.charm = charm
        self.wit = wit
        self.attunement = attunement

    def __repr__(self):
        return f"owner_id: {self.owner_id}, stat_id: {self.stat_id}"


class Inventory(Base):
    __tablename__ = "character_inventories"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), primary_key=True, nullable=False)
    max_weight = Column(Integer, nullable=False)
    items = relationship("PlayerItem", backref="owner")

    def __init__(self, owner_id, max_weight, items):
        self.owner_id = owner_id
        self.max_weight = max_weight
        self.items = items
    
    def __repr__(self):
        return f"owner_id: {self.owner_id}, max_weight: {self.max_weight}, items: {self.items}"
        

class PlayerItem(Base):
    __tablename__ = "character_items"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), nullable=False)
    item_id = Column(String(60), nullable=False, unique=True, primary_key=True)
    item_name = Column(String(40), nullable=False)
    quantity = Column(Integer)
    # Move data bellow from player database to game database
    # item_img = Column(BLOB)
    # item_type = Column(String(40), nullable=False)
    # item_subtype = Column(String(200))
    # item_desc = Column(String(400))
    # item_value = Column(Integer)
    # item_condition = Column(String(60))
    # item_weight = Column(Integer)
    # stat_roll = Column(String(200))
    # energy_cost = Column(Integer)

    def __init__(self, owner_id, item_id, item_name, quantity):
        self.owner_id = owner_id
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity

    def __repr__(self):
        return f"item_id: {self.item_id}, quantity: {self.quantity}"

class Affiliation(Base):
    __tablename__ = "character_affiliations"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), nullable=False)
    faction_name = Column(String(60), nullable=False)
    faction_id = Column(String(60), nullable=False, unique=True)
    reputation = Column(Integer, nullable=False)

    def __init__(self, owner_id, faction_name, faction_id, reputation):
        self.owner_id = owner_id
        self.faction_name = faction_name
        self.faction_id = faction_id
        self.reputation = reputation

    def __repr__(self):
        return f"owner_id: {self.owner_id}, faction_id: {self.faction_id}, reputation: {self.reputation}"

class StatusFx(Base):
    __tablename__ = "character_status_effects"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), nullable=False)
    fx_id = Column(String(60), nullable=False, primary_key=True)
    fx_name = Column(String(60), nullable=False)

class Perk(Base):
    __tablename__ = "character_perks"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), nullable=False)
    perk_id = Column(String(60), nullable=False, primary_key=True)
    perk_name = Column(String(60), nullable=False)

class Origin(Base):
    __tablename__ = "character_origin"

    owner_id = Column(String(60), ForeignKey("characters.char_id"), nullable=False)
    character_desc = Column(String(400))
    affinities = relationship("affinity", backref="owner")
    ailments = relationship("ailment", backref="owner")
    quirks = relationship("quirk", backref="owner")



Engine = create_engine(url="sqlite:///jack-of-all-trades/backend/Database/player_database.db", echo=True)
Base.metadata.create_all(bind=Engine)
        
Session = sessionmaker(bind=Engine)
session = Session()
