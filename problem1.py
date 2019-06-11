#!/usr/bin/python3

#give the date whenturn 95
import datetime
name=input("Enter Your Name :")
age=int(input("Enter your age :"))
present = datetime.datetime.now()
print(name," Will turn 95 in ",(95-age)+present.year)

