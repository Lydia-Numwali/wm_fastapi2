from pydantic import BaseModel

# WasteItem Schemas
class WasteItemBase(BaseModel):
    category: str
    description: str
    weight: float
    disposal_method: str
    assigned_collector_id: int | None  # Optional reference to a collector

class WasteItemCreate(WasteItemBase):
    pass

class WasteItem(WasteItemBase):
    id: int

    class Config:
        orm_mode = True

# WasteCollector Schemas
class WasteCollectorBase(BaseModel):
    name: str
    contact_info: str
    assigned_zone: str  # Zone assigned to the collector

class WasteCollectorCreate(WasteCollectorBase):
    pass

class WasteCollector(WasteCollectorBase):
    id: int

    class Config:
        orm_mode = True
