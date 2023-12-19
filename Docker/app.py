from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pandas as pd 

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
