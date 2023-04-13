from fastapi import FastAPI, Depends
from routes.tickets import tickets_router
from routes.business_services import business_services_router
from db import get_redis


app = FastAPI()

app.include_router(tickets_router)
app.include_router(business_services_router)

@app.on_event("startup")
async def startup_event():
    app.state.redis = get_redis()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()