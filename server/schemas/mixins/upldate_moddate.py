from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
# from dateutil import tz
# import pytz


class UpldateModdateOut(BaseModel):
    moddate: Optional[datetime] = None
    upldate: datetime

    upldate_formatted_local: Optional[str] = None
    upldate_or_moddate_formatted_for_local: Optional[str] = None

class UpldateModdateCreate(BaseModel):
    moddate: Optional[datetime] = None
    upldate: datetime = datetime.now(timezone.utc)

class UpldateModdateUpdate(BaseModel):
    moddate: datetime = datetime.now(timezone.utc)