import requests
from collections import defaultdict
import mysql.connector
from django.shortcuts import render
from django.conf import settings
import MySQLdb
import json
import datetime
import mysql.connector
from nested_lookup import nested_lookup
import collections
import csv
from GIDP.Scripts.Store import Salesforce
basepath = settings.BASE_DIR


# Create your views here.


def SFDCreport(request):

    dbconn = MySQLdb.connect(database='Gidp', user='gidp', password='Gidp@123', host='10.235.21.123')
    query1 = "select * from sfdc1;"
    with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(query1)
        data = cursor.fetchall()
    context = {"data": data,"fail": 'objectlink'}
    return render(request, basepath + '/GIDP/templates/Salesforce1.html', context)


def Mulereport(request):
    dbconn = MySQLdb.connect(database='Gidp', user='gidp', password='Gidp@123', host='10.235.21.123')
    query1 = "select * from mule1;"
    with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(query1)
        data = cursor.fetchall()
    context = {"data": data,"fail": 'MulesoftRequest',"fail1": 'SalesforceResponse'}
    return render(request, basepath + '/GIDP/templates/mulesoft.html', context)

def Eventreport(request):
    dbconn = MySQLdb.connect(database='Gidp', user='gidp', password='Gidp@123', host='10.235.21.123')
    query1 = "select * from sfdc1;"
    with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(query1)
        data = cursor.fetchall()
    context = {"data": data,"fail": 'objectlink'}
    return render(request, basepath + '/GIDP/templates/Salesforce1.html', context)