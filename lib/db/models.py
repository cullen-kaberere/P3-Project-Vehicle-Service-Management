from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# Vehicles Table
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    owner_name = Column(String)
       
       
    def __repr__(self):
        return f"<Vehicle(id={self.id}, make={self.make}, model={self.model}, year={self.year}, owner={self.owner_name})>"

# Mechanics Table
class Mechanic(Base):
    __tablename__ = 'mechanics'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)

    def __repr__(self):
        return f"<Mechanic(id={self.id}, name={self.name}, specialty={self.specialty})>"



# Services Table
class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    mechanic_id = Column(Integer, ForeignKey('mechanics.id'))
    date = Column(String)
    description = Column(String)

    vehicle = relationship("Vehicle")
    mechanic = relationship("Mechanic")

    def __repr__(self):
        return f"<Service(id={self.id}, vehicle_id={self.vehicle_id}, mechanic_id={self.mechanic_id}, date={self.date}, description={self.description})>"
