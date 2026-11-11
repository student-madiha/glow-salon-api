from sqlalchemy import select

from app.database import SessionLocal
from app.models import Treatment

starting_treatments = [
    {"name": "Haircut", "price": 50, "minutes": 30},
    {"name": "Hair Colour", "price": 150, "minutes": 90},
    {"name": "Manicure", "price": 40, "minutes": 45},
    {"name": "Facial", "price": 120, "minutes": 60},
]

db = SessionLocal()

for item in starting_treatments:
    existing = db.scalars(
        select(Treatment).where(Treatment.name == item["name"])
    ).first()
    if existing is None:
        db.add(Treatment(**item))
        print("Added:", item["name"])
    else:
        print("Already there:", item["name"])

db.commit()
db.close()

print("✅ Treatments ready!")