import random
import time

def randomdate(startdate,enddate):
    print("printing random date between ",startdate,"and",enddate)
    rando=random.random()
    dateformat='%m/%d/%y'
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+rando*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))

    print("random date = ",randomdate("1/4/2025","12/12/2025"))
randomdate()