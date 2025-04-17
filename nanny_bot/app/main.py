from fastapi import FastAPI

from .db import engine, Base
from .routers import users, sitters, pets, bookings

app = FastAPI(title="Pet Sitter Bot Backend")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(users.router)
app.include_router(sitters.router)
app.include_router(pets.router)
app.include_router(bookings.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
