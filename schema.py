from pydantic import BaseModel , Field

class FairInput(BaseModel):
    distance_km: float = Field(..., gt=0, le=60)
    passenger_count: int = Field(..., ge=1, le=6)
    hour: int = Field(..., ge=0, le=23)
    weekday: int = Field(..., ge=0, le=6)
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., ge=2009, le=2015)
