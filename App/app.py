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

@app.route('/patients')
def patients():
    return render_template('patients.html')
    
    @app.route('/providers')
def providers():
    return render_template('providers.html')

    @app.route('/appointments')
def appointments():
    return render_template('appointments.html')

    @app.route('/test')
def test():
    return render_template('test.html')

    @app.route('/prescriptions')
def prescriptions():
    return render_template('prescriptions.html')
    


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )