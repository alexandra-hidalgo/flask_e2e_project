from flask import Flask, render_template, request
import sentry_sdk
from sqlalchemy import create_engine
import pandas as pd 


sentry_sdk.init(
    dsn="https://b4cde95c167fcdfb029d5d9f386ff3cd@o4506300835692546.ingest.sentry.io/4506420347535360",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

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

@app.route('/error')
def creating_error():
    try:
        1/0
    except Exception as e:
        raise Exception (f'something is not right: {e}')    

@app.route('/error2')
def creating_error2():
    try:
        500/20
    except Exception as e:
        raise Exception (f'this is the second example: {e}')   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


