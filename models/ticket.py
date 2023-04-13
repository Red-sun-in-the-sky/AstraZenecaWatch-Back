from pydantic import BaseModel

class Ticket(BaseModel):
    sys_id: str
    Business_Service: str
    number: str
    short_description: str
    priority: str
    status: str
    system_status: str