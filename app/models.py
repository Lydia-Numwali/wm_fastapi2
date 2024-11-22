# app/models.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class WasteItem(Base):
    __tablename__ = "waste_items"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)  # E.g., Plastic, Organic, E-waste
    description = Column(String, index=True)
    weight = Column(Float)  # Weight in kilograms
    disposal_method = Column(String)  # E.g., Recycle, Compost, Incinerate
