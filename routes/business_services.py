from fastapi import APIRouter, Depends
from typing import List
from db import get_redis
from models.business_group import BusinessGroup
import aioredis
import json

business_services_router = APIRouter(prefix="/business-services")

@business_services_router.get("/", response_model=List[str])
async def get_business_services(redis: aioredis.Redis = Depends(get_redis)) -> List[str]:
    keys = await redis.keys("BG*")
    services = []
    for key in keys:
        bg_data = await redis.get(key)
        bg = BusinessGroup.parse_raw(bg_data)
        services.extend(bg.Business_Services)
    return services
