from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Vehicle, Mechanic, Service
import os

# Initialize database connection
db_path = os.path.join("lib", "db", "vehicle_service.db")
engine = create_engine(f"sqlite:///{db_path}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



# Seed data
vehicles = [
    Vehicle(make="Toyota", model="Prado", year=2015, owner_name="Cullen Kaberere"),
    Vehicle(make="Mazda", model="Axela", year=2018, owner_name="Natalie Njoki")
]

mechanics = [
    Mechanic(name="John Doe", specialty="Engine Repair"),
    Mechanic(name="Jane Smith", specialty="Brake Specialist")
]

services = [
    Service(vehicle_id=1, mechanic_id=1, date="2024-06-01", description="Oil Change"),
    Service(vehicle_id=2, mechanic_id=2, date="2024-06-03", description="Brake Replacement")
]

# Add to database
session.add_all(vehicles + mechanics + services)
session.commit()

print("Database seeded successfully!")
