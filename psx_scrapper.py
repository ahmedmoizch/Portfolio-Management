import mysql.connector
import pandas as pd
from datetime import datetime

# time Now
now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M")


#Local DataBase
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio'
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

df = pd.read_csv('psx_data.csv')
data = df[['SYMBOL','CURRENT','VOLUME']]

for index, row in data.iterrows():
    symbol = row['SYMBOL']
    current = row['CURRENT']
    volume = row['VOLUME']
    cursor.execute("INSERT INTO psx_history (symbol, time_stamp, current_price, volume) VALUES (%s, %s,%s ,%s)", (symbol,time,current,volume))


#insert into historic_data_psx values("Ahmed")
connection.commit()

cursor.close()
connection.close()


