from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Vehicle, Mechanic, Service
import os

# Initialize database connection
db_path = os.path.join("lib", "db", "vehicle_service.db")
engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
session = Session()

def add_vehicle():
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    year = input("Enter vehicle year: ")
    owner = input("Enter owner's name: ")

    vehicle = Vehicle(make=make, model=model, year=year, owner_name=owner)
    session.add(vehicle)
    session.commit()
    print("Vehicle added successfully!")

def add_mechanic():
    name = input("Enter mechanic's name: ")
    specialty = input("Enter mechanic's specialty: ")

    mechanic = Mechanic(name=name, specialty=specialty)
    session.add(mechanic)
    session.commit()
    print("Mechanic added successfully!")

def schedule_service():
    vehicle_id = input("Enter vehicle ID: ")
    mechanic_id = input("Enter mechanic ID: ")
    date = input("Enter service date (YYYY-MM-DD): ")
    description = input("Enter service description: ")

    service = Service(vehicle_id=vehicle_id, mechanic_id=mechanic_id, date=date, description=description)
    session.add(service)
    session.commit()
    print("Service scheduled successfully!")

def view_vehicles():
    vehicles = session.query(Vehicle).all()
    for vehicle in vehicles:
        print(vehicle)

def view_mechanics():
    mechanics = session.query(Mechanic).all()
    for mechanic in mechanics:
        print(mechanic)

def view_services():
    services = session.query(Service).all()
    for service in services:
        print(service)

def main_menu():
    while True:
        print("\nVehicle Service Management System")
        print("1. Add Vehicle")
        print("2. Add Mechanic")
        print("3. Schedule Service")
        print("4. View Vehicles")
        print("5. View Mechanics")
        print("6. View Services")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_vehicle()
        elif choice == "2":
            add_mechanic()
        elif choice == "3":
            schedule_service()
        elif choice == "4":
            view_vehicles()
        elif choice == "5":
            view_mechanics()
        elif choice == "6":
            view_services()
        elif choice == "7":
            print("Thank You! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
