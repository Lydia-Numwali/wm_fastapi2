from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, Base, get_db

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/waste_items/", response_model=schemas.WasteItem)
def create_waste_item(waste_item: schemas.WasteItemCreate, db: Session = Depends(get_db)):
    return crud.create_waste_item(db=db, waste_item=waste_item)

@app.get("/waste_items/", response_model=list[schemas.WasteItem])
def read_waste_items(db: Session = Depends(get_db)):
    return crud.get_waste_items(db=db)

@app.get("/waste_items/{item_id}", response_model=schemas.WasteItem)
def read_waste_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_waste_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Waste item not found")
    return db_item

@app.put("/waste_items/{item_id}", response_model=schemas.WasteItem)
def update_waste_item(item_id: int, waste_item: schemas.WasteItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_waste_item(db=db, item_id=item_id, waste_item=waste_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Waste item not found")
    return db_item

@app.delete("/waste_items/{item_id}")
def delete_waste_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_waste_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Waste item not found")
    return {"message": "Waste item deleted"}
