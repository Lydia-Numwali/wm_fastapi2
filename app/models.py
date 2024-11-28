from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WasteItem(Base):
    __tablename__ = "waste_items"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)  # E.g., Plastic, Organic, E-waste
    description = Column(String, index=True)
    weight = Column(Float)  # Weight in kilograms
    disposal_method = Column(String)  # E.g., Recycle, Compost, Incinerate
    assigned_collector_id = Column(Integer, ForeignKey('waste_collectors.id'), nullable=True) 

# WasteCollector Model
class WasteCollector(Base):
    __tablename__ = "waste_collectors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String, index=True)
    assigned_zone = Column(String, index=True)  # E.g., Zone A, Zone B
