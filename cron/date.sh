#! /bin/bash
i=$(date +'%D-%T')
echo "${i}">>/home/gerrhorr/DT.txt

#crontab
# 0 */1 * * * bash /PycharmProjects/python-education/cron/date.sh


