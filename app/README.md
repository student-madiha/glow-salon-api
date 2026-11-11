# Glow Salon API

A booking API for a salon, built with FastAPI and PostgreSQL.
Customers can view treatments, make bookings, look them up, and cancel them.

## Tech used

- Python and FastAPI
- PostgreSQL (database)
- SQLAlchemy (connects Python to the database)
- Pydantic (checks the data that comes in)
- Uvicorn (runs the server)

## Project structure

- `app/main.py`: starts the app and plugs in the routers
- `app/routes/`: the endpoints (URLs)
- `app/schemas/`: Pydantic schemas for data coming in and going out
- `app/services/`: the business rules
- `app/models/`: SQLAlchemy models (the database tables)
- `app/database.py`: the database connection and sessions
- `create_tables.py`: creates the tables
- `add_treatments.py`: adds the starting treatments

## Setup

1. Create a PostgreSQL database `salon_db` with a login role `salon_user`.
2. Create a `.env` file in the project folder:
   ```
   DATABASE_URL=postgresql+psycopg://salon_user:YOUR_PASSWORD@localhost:5432/salon_db
   ```
3. Create and activate a virtual environment, then install the packages:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. Create the tables and add the treatments:
   ```bash
   python create_tables.py
   python add_treatments.py
   ```
5. Run the server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```
6. Open http://localhost:8000/docs

## Endpoints

| Method | URL | What it does |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/treatments` | List all treatments |
| GET | `/treatments/{id}` | Get one treatment |
| POST | `/bookings` | Make a booking |
| GET | `/bookings` | List all bookings |
| GET | `/bookings/{id}` | Get one booking |
| DELETE | `/bookings/{id}` | Cancel a booking |

## Booking rules

| Rule | Error |
|---|---|
| The treatment must exist | 404 |
| The date can't be in the past | 400 |
| No two bookings in the same time slot | 409 |
| Missing or wrong data | 422 |

Rules 1 and 3 are also enforced by the database
(a foreign key and a unique constraint).

## Run with Docker (easiest)

You only need Docker Desktop installed. No Python or PostgreSQL needed.

1. Create a `.env` file in the project folder:
   ```
   POSTGRES_USER=salon_user
   POSTGRES_PASSWORD=YOUR_PASSWORD
   POSTGRES_DB=salon_db
   ```
2. Start the app and database:
   ```bash
   docker compose up -d --build
   ```
3. Create the tables and add the treatments (first time only):
   ```bash
   docker compose exec api python create_tables.py
   docker compose exec api python add_treatments.py
   ```
4. Open http://localhost:8000/docs
5. To stop: `docker compose down`