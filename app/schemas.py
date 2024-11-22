# app/schemas.py
from pydantic import BaseModel

class WasteItemBase(BaseModel):
    category: str
    description: str
    weight: float
    disposal_method: str

class WasteItemCreate(WasteItemBase):
    pass

class WasteItem(WasteItemBase):
    id: int

    class Config:
        orm_mode = True
