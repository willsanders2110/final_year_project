import sqlite3

conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE moisture_data
             (time, plant_1, plant_2, plant_3, plant_4)''')

conn.commit()
conn.close()