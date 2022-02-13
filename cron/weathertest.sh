#! /bin/bash
curl -o /home/gerrhorr/weather.json "https://api.openweathermap.org/data/2.5/weather?lat=50&lon=36&appid=7ed915479d5c088ffd10991650e16531"

#crontab
#0 12 * * * bash /PycharmProjects/python-education/cron/weathertest.sh

