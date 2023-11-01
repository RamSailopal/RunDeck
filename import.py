#!/usr/bin/python3
"""Script to sync repo changes with RunDeck jobs"""
import os
import re
import requests # # pylint: disable=import-error
PROJECT="Test"
TOKEN=os.getenv("RUNDECK_KEY")
#
#   First check for new jobs
#
ADDR="http://localhost:4440/api/15/project/" + PROJECT + \
    "/scm/import/action/import-jobs/input"
resp=requests.get(ADDR, headers={'Accept': 'application/json',
                                 'X-Rundeck-Auth-Token': TOKEN,
                                 'Content-Type': 'application/json'}, timeout=10)
jsonobj=resp.json()
items=[]
for item in jsonobj['importItems']:
    if item['tracked'] is False:
        items.append(item['itemId'])
if len(items) > 0:
    ADDR1="http://localhost:4440/api/14/project/Test/scm/import/action/import-jobs"
    DATA={"items":items}
    resp1=requests.post(ADDR1, headers={'X-Rundeck-Auth-Token': TOKEN,
                                        'Content-Type': 'application/json'}, json=DATA, timeout=10)
#
#   Now process any job updates
#
ADDR="http://localhost:4440/api/25/project/" + PROJECT + "/jobs/export"
resp=requests.get(ADDR, headers={'X-Rundeck-Auth-Token': TOKEN,
                                 'Content-Type': 'application/json'}, timeout=10)
matches=re.findall("<id>.*</id>",resp.text)
for match in matches:
    newstr=match.replace("/", "")
    newstr1=newstr.split("<id>")
    JOB=newstr1[1]
    ADDR1="http://localhost:4440/api/14/job/" + JOB + "/scm/import/action/import-jobs"
    DATA={"input":{"message": "test"}}
    resp1=requests.post(ADDR1, headers={'X-Rundeck-Auth-Token': TOKEN,
                                        'Content-Type': 'application/json'}, json=DATA, timeout=10)
    print(resp1.text)
