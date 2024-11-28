from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, Base, get_db

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Waste Item Endpoints
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

# Waste Collector Endpoints
@app.post("/waste_collectors/", response_model=schemas.WasteCollector)
def create_waste_collector(waste_collector: schemas.WasteCollectorCreate, db: Session = Depends(get_db)):
    return crud.create_waste_collector(db=db, waste_collector=waste_collector)

@app.get("/waste_collectors/", response_model=list[schemas.WasteCollector])
def read_waste_collectors(db: Session = Depends(get_db)):
    return crud.get_waste_collectors(db=db)

@app.get("/waste_collectors/{collector_id}", response_model=schemas.WasteCollector)
def read_waste_collector(collector_id: int, db: Session = Depends(get_db)):
    db_collector = crud.get_waste_collector(db=db, collector_id=collector_id)
    if db_collector is None:
        raise HTTPException(status_code=404, detail="Waste collector not found")
    return db_collector
