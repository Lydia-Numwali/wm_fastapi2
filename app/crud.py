from sqlalchemy.orm import Session
from app import models, schemas

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
