#!/usr/bin/python

import MySQLdb
import os

miConexion = MySQLdb.connect( host='gps.igromi.com', user= 'traccar', passwd='Traccar12!', db='traccar' )
cur = miConexion.cursor()

#gps app celu Oscar

unique_id='9170537657'
token='gps_inia_1'

cur.execute( "SELECT latitude, longitude,altitude,speed,servertime FROM tc_positions WHERE deviceid=(select id from tc_devices where uniqueid='"+unique_id+"') order by servertime desc limit 1" )
for latitude, longitude ,altitude,speed,servertime in cur.fetchall() :
    print(latitude, longitude,altitude,speed,servertime)

os.system('curl -v -X POST -d "{\"latitude\":'+str(latitude)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
os.system('curl -v -X POST -d "{\"longitude\":'+str(longitude)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
os.system('curl -v -X POST -d "{\"altitude\":'+str(altitude)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')
os.system('curl -v -X POST -d "{\"speed\":'+str(speed)+'}" iot.igromi.com:8080/api/v1/'+token+'/telemetry --header "Content-Type:application/json"')



miConexion.close()