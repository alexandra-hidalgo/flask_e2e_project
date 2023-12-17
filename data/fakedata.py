import pandas as pd 
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
import faker 
import sqlite3

##
db_host = '4.227.178.200'
user = 'alexa'
password='rada2023'
database='MedBooking'

## using mysql+pymysql
engine = create_engine(f"mysql+pymysql://{user}:{password}@{db_host}/{database}")

## get tables from database
sql_query_1 = "SHOW TABLES"
tables = pd.read_sql(sql_query_1, engine)

# create fake data
# inside of a patients table, create First_name, Last_name, Date_of_birth (date), Gender, Phone<number, and Insurance_provider

fake = faker.Faker()


############################################################
############################################################
##### THIS SECTION IS FOR THE FAKE PATIENTS TABLE #####
# create a list of 1000 fake patients
patients_fake = []

for i in range(100):
    First_name = fake.first_name()
    Last_name = fake.last_name()
    Date_of_birth = fake.date()
    ## select between M/F for gender
    Gender = fake.random_element(elements=('M', 'F'))
    Phone = fake.msisdn()
    Insurance_provider = fake.random_element(elements=('Aetna', 'Blue Cross', 'Cigna', 'Humana', 'United Health'))
    ## save into patient dictionary 
    patient = {
        'First_name': First_name,
        'Last_name': Last_name,
        'Date_of_birth': Date_of_birth,
        'Gender': Gender,
        'Phone_number': Phone,
        'Insurance_provider': Insurance_provider
    }
    print(patient)
    ## add patient to dataframe
    patients_fake.append(patient)

## loop through each item in patients and add to dataframe
fake_patients = pd.DataFrame(patients_fake)
############################################################
############################################################
############################################################



## then to send fake data oer to Patients table 
fake_patients.to_sql('Patients', engine, if_exists='append', index=False)
fake_providers.to_sql('Providers', engine, if_exists='append', index=False)
fake_providers.to_sql('Providers', engine, if_exists='append', index=False)
fake_providers.to_sql('Providers', engine, if_exists='append', index=False)
fake_providers.to_sql('Providers', engine, if_exists='append', index=False)
fake_providers.to_sql('Providers', engine, if_exists='append', index=False)


##### THIS SECTION IS FOR THE FAKE PROVIDERS TABLE #####
# create a list of 100 fake providers
providers_fake = []

for i in range(100):
    First_name = fake.first_name()
    Last_name = fake.last_name()
    Specialty = fake.random_element(elements=('Cardiology', 'Internal Medicine', 'Pediatrics', 'Oncology', 'Gastroenterology'))
    Working_hours = fake.random_element(elements=('7-2', '9-5', '10-6','11-4'))
    Consultation_fee = fake.random_element(elements=('30', '50', '100'))
    ## save into providers dictionary 
    provider = {
        'First_name': First_name,
        'Last_name': Last_name,
        'Specialty': Specialty,
        'Working_hours': Working_hours,
        'Consultation_fee': Consultation_fee
    }
    print(provider)
    ## add patient to dataframe
    providers_fake.append(provider)

## loop through each item in patients and add to dataframe
fake_providers = pd.DataFrame(providers_fake)

fake_providers.to_sql('Providers', engine, if_exists='append', index=False)


##### THIS SECTION IS FOR THE FAKE APPOINTMENTS TABLE #####
# create a list of 100 fake appointments
appointments_fake = []

for i in range(100):
    Patient_id = fake.random_element(digits=2)
    Provider_id = fake.random_element(digits=2)
    Appointment_datetime = fake.date_between_dates()
    Status = fake.random_element(elements=('Schedule', 'Canceled', 'Rescheduled', 'Arrived', 'In Progress', 'No Show'))
    Appointment_reason = fake.random_element(elements=('Consultation', 'Start Treatment', 'Second Opinion', 'Pain Management' 'Vaccination', ''))
    Appointment_notes = fake.random_element(elements=('Dietary Advice', 'Medication Adherence', 'Smoking Cessation Advice', 'Preventive Recommendations', 'mental Health Support'))
    ## save into patient dictionary 
    appointment = {
        'Patient_id': Patient_id,
        'Provider_id': Provider_id,
        'Appointment_datetime': Appointment_datetime,
        'Status': Status,
        'Appointment_reason': Appointment_reason,
        'Appointment_notes': Appointment_notes
    }
    print(appointment)
    ## add patient to dataframe
    appointments_fake.append(appointment)

## loop through each item in patients and add to dataframe
fake_appointments = pd.DataFrame(appointments_fake)

fake_appointments.to_sql('Appointments', engine, if_exists='append', index=False)

# THIS SECTION IS THE FAKE TEST TABLE
# create a list of 100 fake test
test_fake = []

for i in range(100):
    Appointment_id = fake.random_number(digits=2)
    Test_name = fake.random_element(elements=('Blood Glucose test', 'Hemoglobin A1c', 'Urinalysis', 'Liver Function Test', 'Thyrid Function Test', 'Complete Blood Count'))
    Results = fake.random_element(elements=('Normal Range', 'Abnormal Range', 'Needs to Repeat'))
    ## save into patient dictionary 
    test = {
        'Appointment_id': Appointment_id,
        'Test_name': Test_name,
        'Results': Results
    }
    print(test)
    ## add patient to dataframe
    test_fake.append(test)

## loop through each item in patients and add to dataframe
fake_test = pd.DataFrame(test_fake)

fake_test.to_sql('Test', engine, if_exists='append', index=False)

##### THIS SECTION IS FOR THE FAKE PRESCRIPTION TABLE #####
# create a list of 100 fake prescriptions
prescriptions_fake = []

for i in range(100):
    Appointment_id = fake.random_number(digits=2)
    Prescribing_provider_id = fake.random_number(digits=2)
    Medication_name = fake.random_element(elements=('Albuterol', 'Metformin', 'Omeprazole', 'Losartan', 'Amoxicillin', 'Atorvastatin', 'Acetaminophen', 'Metoprolol', 'Ibuprofen'))
    Dosage = fake.random_element(elements=('10mg', '25mg', '80mg', '250mg', '500mg', '800mg'))
    Instructions = fake.random_element(elements=('Take Twice Daily', 'By Mouth Every 8 Hours', 'By Mouth every 4 Hours', "Once a Day"))
    ## save into prescription dictionary 
    prescriptions = {
        'Appointment_id': Appointment_id,
        'Prescribing_provider_id': Prescribing_provider_id,
        'Medication_name': Medication_name,
        'Dosage': Dosage,
        'Instructions': Instructions
    }
    print(prescriptions)
    ## add patient to dataframe
    prescriptions_fake.append(prescriptions)

## loop through each item in patients and add to dataframe
fake_prescriptions = pd.DataFrame(prescriptions_fake)

fake_prescriptions.to_sql('Prescriptions', engine, if_exists='append', index=False)
############################################################


        

        