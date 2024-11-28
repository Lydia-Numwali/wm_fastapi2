from sqlalchemy.orm import Session
from app import models, schemas
# CRUD for Waste Items
def get_waste_items(db: Session):
    return db.query(models.WasteItem).all()

def get_waste_item(db: Session, item_id: int):
    return db.query(models.WasteItem).filter(models.WasteItem.id == item_id).first()

def create_waste_item(db: Session, waste_item: schemas.WasteItemCreate):
    db_item = models.WasteItem(**waste_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_waste_item(db: Session, item_id: int, waste_item: schemas.WasteItemCreate):
    db_item = db.query(models.WasteItem).filter(models.WasteItem.id == item_id).first()
    if db_item:
        for key, value in waste_item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_waste_item(db: Session, item_id: int):
    db_item = db.query(models.WasteItem).filter(models.WasteItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

# CRUD for Waste Collectors
def get_waste_collectors(db: Session):
    return db.query(models.WasteCollector).all()

def get_waste_collector(db: Session, collector_id: int):
    return db.query(models.WasteCollector).filter(models.WasteCollector.id == collector_id).first()

def create_waste_collector(db: Session, waste_collector: schemas.WasteCollectorCreate):
    db_collector = models.WasteCollector(**waste_collector.dict())
    db.add(db_collector)
    db.commit()
    db.refresh(db_collector)
    return db_collector

def update_waste_collector(db: Session, collector_id: int, waste_collector: schemas.WasteCollectorCreate):
    db_collector = db.query(models.WasteCollector).filter(models.WasteCollector.id == collector_id).first()
    if db_collector:
        for key, value in waste_collector.dict().items():
            setattr(db_collector, key, value)
        db.commit()
        db.refresh(db_collector)
    return db_collector

def delete_waste_collector(db: Session, collector_id: int):
    db_collector = db.query(models.WasteCollector).filter(models.WasteCollector.id == collector_id).first()
    if db_collector:
        db.delete(db_collector)
        db.commit()
    return db
