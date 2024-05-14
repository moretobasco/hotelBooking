from pydantic import BaseModel, ConfigDict


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: [list[str]]
    rooms_quantity: int
    image_id: int

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
