#!/usr/bin/env python
from weather import weather
import datetime
import sys

if(len(sys.argv)<2):
	print 'Error: use format--> ./sample.py "enter you city name here"'
else:
	city = weather(sys.argv[1])
	print 'Weather |',city.name,city.country,'at',
	print (datetime.datetime.fromtimestamp(int(city.dt)).strftime('%H:%M:%S %m-%d-%Y '))
	print '------------------------------------------'
	print '\t','Temp:',city.temp,'Celsius'
	print '\t','Temp(min,max):','(',city.temp_min,',',city.temp_max,')','Celsius'
	print '\t','Pressure:',city.pressure,'hPa'
	print '\t','Humidity:',city.humidity,'%'
	print '\t',city.sky
	print '\t','Clouds %:',city.cloud
	print '\t','Wind speed:',city.wind ,'mps'
