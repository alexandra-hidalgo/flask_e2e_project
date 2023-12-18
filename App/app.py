from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

db_ip = '4.227.178.200'
db_port = '3306'
db_username = 'alexa'
db_password = 'rada2023'
db_name = 'MedBooking'

engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_ip}:{db_port}/{db_name}')

## get tables from database
sql_query_1 = "SHOW TABLES"
tables = pd.read_sql(sql_query_1, engine)

@app.route('/')
def index():
    return render_template('base.html')

df = pd.read_sql('SELECT * FROM MedBooking.Patients', engine)
@app.route('/data')
def data(data=df):
    return render_template('data.html', data=data)

df = pd.read_sql('SELECT * FROM MedBooking.Providers', engine)
@app.route('/providers')
def providers(data=df):
    return render_template('providers.html', data=data)

df = pd.read_sql('SELECT * FROM MedBooking.Appointments', engine)
@app.route('/appointments')
def appointments(data=df):
    return render_template('appointments.html', data=data)

df = pd.read_sql('SELECT * FROM MedBooking.Test', engine)
@app.route('/test')
def test(data=df):
    return render_template('test.html', data=data)

df = pd.read_sql('SELECT * FROM MedBooking.Prescriptions', engine)
@app.route('/prescriptions')
def prescriptions(data=df):
    return render_template('prescriptions.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )