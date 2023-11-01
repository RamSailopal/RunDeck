#!/usr/bin/python3
import requests
import re
PROJECT="Test"
TOKEN="eXLnU4c3Hx5udUyWJiLX80rGKxQzmvK8"
ADDR="http://localhost:4440/api/25/project/" + PROJECT + "/jobs/export"
resp=requests.get(ADDR, headers={'X-Rundeck-Auth-Token': TOKEN, 'Content-Type': 'application/json'})
matches=re.findall("<id>.*</id>",resp.text)
for match in matches:
    newstr=match.replace("/", "")
    newstr1=newstr.split("<id>")
    JOB=newstr1[1]
    ADDR1="http://localhost:4440/api/14/job/" + JOB + "/scm/import/action/import-jobs"
    DATA={"input":{"message": "test"}}
    resp1=requests.post(ADDR1, headers={'X-Rundeck-Auth-Token': TOKEN, 'Content-Type': 'application/json'}, json=DATA)
    print(resp1.text)
