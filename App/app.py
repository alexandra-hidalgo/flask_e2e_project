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

@app.route('/')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
