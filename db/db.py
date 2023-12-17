from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patients(Base):
    __tablename__ = 'patients'

Patient_id = Column(Integer, primary_key=True)
First_name = Column(String(50), nullable=False)
last_name = Column(String(50), nullable=False)
date_of_birth = Column(Date, nullable=False)
gender = Column(String(10), nullable=False)
phone_number = Column(String(15), nullable=False)
insurance_provider = Column(String(50))

class Providers(Base):
    __tablename__ = 'Providers' 

provider_id = Column(Integer, primary_key=True)
filterirst_name = Column(String(50), nullable=False)
last_name = Column(String(50), nullable=False)
specialty = Column(String(50), nullable=False)
working_hours = Column(String(100), nullable=False)
consultation_fee = Column(String(50), nullable=False)

Providers = relationship('Appointments', back_populates='Providers')
Patients = relationship('Appointments', back_populates='Patients')

class Appointments(Base):
    __tablename__ = 'Appointments'

appointment_id = Column(Integer, primary_key=True)
patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
Provider_id = Column(Integer, ForeignKey('provider.id'), nullable=False)
Appointment_datetime = Column(Date, nullable=False)
Status = Column(String(50), nullable=False)
Appointment_reason = Column(String(50), nullable=False)
Appointment_notes = Column(String(50), nullable=False)

Appointments = relationship('Test', back_populates='Appointments')

class Test(Base):
    __tablename__ = 'test'

Test_id = Column(Integer, primary_key=True)
Appointment_id = Column(Integer, ForeignKey('appointment.id'), nullable=False)
Test_name = Column(String(50), nullable=False)
Results = Column(String(50), nullable=False)

class Prescriptions(Base):
    __tablename__ = 'Prescriptions'

Prescription_id = Column(Integer, primary_key=True)
Appointment_id = Column(Integer, ForeignKey('appointment.id'), nullable=False)
Prescribing_provider_id = Column(String(50), nullable=False)
Medication_name = Column(String(50), nullable=False)
Dosage = Column(String(50), nullable=False)
Instructions = Column(String(50), nullable=False)

Appointments = relationship('Prescriptions', back_populates='Appointments')
Providers = relationship('Prescriptions', back_populates='Providers')

## create connection and tables
DATABASE_URL = "mysql+mysqlconnector://alexa:rada2023@scratch-server:3306/MedBooking"
DATABASE_URL = "sqlite:///local.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)