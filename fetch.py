import random
from faker import Faker
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import Base, engine, get_db  # Import your database setup and dependencies
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

# Faker setup
fake = Faker()

# Number of records to generate
num_waste_collectors = 100  # Adjust this as needed
num_waste_items = 1000  # Adjust this as needed

# Define WasteCollectors table
class WasteCollector(Base):
    __tablename__ = "waste_collectors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), index=True)
    contact_info = Column(String(length=255), index=True)
    assigned_zone = Column(String(length=255), index=True)
    waste_items = relationship("WasteItem", back_populates="collector")  # For relationship mapping


# Define WasteItems table
class WasteItem(Base):
    __tablename__ = "waste_items"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(length=255), index=True)
    description = Column(String(length=255), index=True)
    weight = Column(Float)
    disposal_method = Column(String(length=255))
    assigned_collector_id = Column(Integer, ForeignKey("waste_collectors.id"), nullable=True)
    collector = relationship("WasteCollector", back_populates="waste_items")  # For relationship mapping


# Create tables in the database
Base.metadata.create_all(bind=engine)


# Generate waste collectors data
def generate_waste_collectors(num_collectors):
    return [
        WasteCollector(
            name=fake.name(),
            contact_info=fake.phone_number(),
            assigned_zone=f"Zone {random.choice(['A', 'B', 'C', 'D'])}"
        )
        for _ in range(num_collectors)
    ]


# Generate waste items data
def generate_waste_items(num_items, db):
    collector_ids = [collector.id for collector in db.query(WasteCollector).all()]
    return [
        WasteItem(
            category=random.choice(["Plastic", "Organic", "E-waste", "Metal", "Glass"]),
            description=fake.text(max_nb_chars=100),
            weight=round(random.uniform(0.5, 50.0), 2),  # Random weight between 0.5kg and 50kg
            disposal_method=random.choice(["Recycle", "Compost", "Incinerate", "Landfill"]),
            assigned_collector_id=random.choice(collector_ids) if collector_ids else None
        )
        for _ in range(num_items)
    ]


# Populate the database
def populate_database():
    with next(get_db()) as db:  # Use the database session dependency
        print("Generating waste collectors data...")
        waste_collectors = generate_waste_collectors(num_waste_collectors)
        db.bulk_save_objects(waste_collectors)
        db.commit()
        print(f"{num_waste_collectors} waste collectors inserted.")

        print("Generating waste items data...")
        waste_items = generate_waste_items(num_waste_items, db)
        db.bulk_save_objects(waste_items)
        db.commit()
        print(f"{num_waste_items} waste items inserted.")


if __name__ == "__main__":
    populate_database()
    print("Data saved to the database.")
