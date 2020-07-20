#!/usr/bin/env python3

import os
import http.client
import json
import urllib.parse

USERNAME = 'chesterm@aetna.com' # os.environ['USERNAME'] #AWS
PASSWORD = ')O9i*U7y^T' # os.environ['PASSWORD'] #AWS
username_encode = ''
password_encode = ''
    
#2020-04-08 02:44:44,376 [638] INFO - [ResultsPublisherService].[RegisterSuccess] Findings for project 546, scan 1372452, were sent to Policy Management

#
# Common Functions
#

def getConnection():
    # Cx username and password
    username_encode = urllib.parse.quote(USERNAME, safe='')
    password_encode = urllib.parse.quote(PASSWORD, safe='')
    
    conn = http.client.HTTPConnection("10.208.191.125")
    return conn

#
# Get details of a specified project.
#
def getScansByProjectId():

    #conn = getConnection()
    # Cx username and password
    username_encode = urllib.parse.quote(USERNAME, safe='')
    password_encode = urllib.parse.quote(PASSWORD, safe='')
    
    conn = http.client.HTTPConnection("10.208.191.125")
    
    # Login for access_token
    payload = "username=" + username_encode + "&password=" + password_encode + "&grant_type=password&scope=sast_rest_api%0A&client_id=resource_owner_client&client_secret=014DF517-39D1-4453-B7B3-9930C563627C"
    headers = {
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
        }
    conn.request("POST", "/cxrestapi/auth/identity/connect/token", payload, headers)

    res = conn.getresponse()
    json_string = res.read().decode("utf-8")
    json_obj = json.loads(json_string)
    token = json_obj['access_token']

    #payload = "{\"NumOfSuccessfulScansToPreserve\":" + str(NUMSCANSTOKEEP) + ",\"durationLimitInHours\":" + str(MAXHOURSTORUN) + "}"

    headers = {
        'Accept': "application/json;v=1.0",
        'Authorization': "Bearer " + token,
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }






#
# Get details of a specified project.
#
def getScansByScanId():

    #conn = getConnection()
    # Cx username and password
    username_encode = urllib.parse.quote(USERNAME, safe='')
    password_encode = urllib.parse.quote(PASSWORD, safe='')
    
    conn = http.client.HTTPConnection("10.208.191.125")

    # Login for access_token
    payload = "username=" + username_encode + "&password=" + password_encode + "&grant_type=password&scope=sast_rest_api%0A&client_id=resource_owner_client&client_secret=014DF517-39D1-4453-B7B3-9930C563627C"
    headers = {
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
        }
    conn.request("POST", "/cxrestapi/auth/identity/connect/token", payload, headers)

    res = conn.getresponse()
    json_string = res.read().decode("utf-8")
    json_obj = json.loads(json_string)
    token = json_obj['access_token']

    headers = {
        'Accept': "application/json;v=1.0",
        'Authorization': "Bearer " + token,
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }


    requestStringScansWithProjectId = "/cxrestapi/auth/teams"
    conn.request("GET", requestStringScansWithProjectId, None, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    outF = open("cxTeams.txt", "w")
    outF.writelines(data.decode("utf-8"))
    outF.close()

    


#getScansByProjectId()
getScansByScanId()
