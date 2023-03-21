from pydantic import BaseModel
from typing import Optional

class CardFilter(BaseModel):
    create_at:Optional[str] = None
    brand:Optional[str] = None
    holder_name:Optional[str] = None
    first_digits:Optional[str] = None
    last_digits:Optional[str] = None
    customer_id : Optional[str] = None
    valid : Optional[bool] = None
    country:Optional[str] = None
    expiration_date : Optional[str] = None
    fingerprint :Optional[str] = None