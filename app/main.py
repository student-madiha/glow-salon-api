from fastapi import FastAPI

from app.routes import treatments, bookings

app = FastAPI(title="Glow Salon")

app.include_router(treatments.router)
app.include_router(bookings.router)


@app.get("/")
def welcome():
    return {"message": "Welcome to Glow Salon!"}