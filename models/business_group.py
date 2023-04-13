from typing import List
from pydantic import BaseModel


class BusinessGroup(BaseModel):
    Business_Group: str
    Business_Services: List[str]