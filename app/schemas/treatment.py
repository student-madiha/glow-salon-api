from pydantic import BaseModel, ConfigDict


class TreatmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: int
    minutes: int