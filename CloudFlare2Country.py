#!/usr/bin/env python
import pandas

#Function to itterate data
def GetServer(number,differencelist):
	locaterlist = list(differencelist)
	locaterlist.sort()
	fastest = locaterlist[number]
	fastestindex = differencelist.index(float(fastest))
	return fastestindex + 1

colnames = ['country', 'status', 'minrply', 'avgrply', 'maxrply','dnsresults'] #CSV column names
DataSet = pandas.read_csv('sample.csv', names=colnames) #Read CSV

#Import CSV Data
country = list(DataSet.country)
status = list(DataSet.status)
minrply = list(DataSet.minrply)
avgrply = list(DataSet.avgrply)
maxrply = list(DataSet.maxrply)
dnsresults = list(DataSet.dnsresults)
difference = list()
fastest = 0
fastestindex = 0

#Remove column name from arrays
minrply = minrply[1:]
maxrply = maxrply[1:]

#Increment calculations for difference
x = 0
for item in minrply:
	difference.append(float(maxrply[x]) - float(minrply[x]))
	x = x + 1 

#Display first 5 servers
for y in range(0,5):
	FastServer = GetServer(y,difference)
	print "Server Location " + str(country[FastServer])
