from fastapi import APIRouter, Depends
from typing import List
from db import get_redis
from models.ticket import Ticket
import aioredis
import json

tickets_router = APIRouter(prefix="/tickets")


@tickets_router.post("/")
async def update_tickets(tickets: List[Ticket], redis: aioredis.Redis = Depends(get_redis)):
    for ticket in tickets:
        await redis.set(ticket.number, ticket.json())
    return {"message": "Tickets updated"}


@tickets_router.get("/", response_model=List[Ticket])
async def get_tickets(redis: aioredis.Redis = Depends(get_redis)) -> List[Ticket]:
    keys = await redis.keys("INC*")
    tickets = []
    for key in keys:
        ticket_data = await redis.get(key)
        tickets.append(Ticket.parse_raw(ticket_data))
    return tickets


@tickets_router.get("/{ticket_number}", response_model=Ticket)
async def get_ticket_by_number(ticket_number: str, redis: aioredis.Redis = Depends(get_redis)) -> Ticket:
    ticket_data = await redis.get(ticket_number)
    return Ticket.parse_raw(ticket_data)
