#!/usr/bin/python

from datetime import datetime, timedelta

now = today = datetime.today()
today = datetime(today.year, today.month, today.day)

print (timedelta(days = 7 - now.weekday() + today - now)).total_seconds()/60
