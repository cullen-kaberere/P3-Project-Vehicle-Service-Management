from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Vehicle, Mechanic, Service
import os

db_path = os.path.join("lib", "db", "vehicle_service.db")
engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
session = Session()

# Fetch and print all vehicles
vehicles = session.query(Vehicle).all()
print("Vehicles:")
for vehicle in vehicles:
    print(vehicle)


# Fetch and print all mechanics
mechanics = session.query(Mechanic).all()
print("\nMechanics:")
for mechanic in mechanics:
    print(mechanic)

# Fetch and print all services
services = session.query(Service).all()
print("\nServices:")
for service in services:
    print(service)
