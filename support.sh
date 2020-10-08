#!/bin/bash
netstat -tulpn | grep :80
echo 'running web server in background ...'
python app.py &

netstat -tulpn | grep :80
echo 'running curl'
curl localhost:8080/newCasesPeak?country=israel