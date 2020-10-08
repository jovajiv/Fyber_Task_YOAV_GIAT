#!/bin/bash
echo 'running web server in background ...'
python app.py &


echo 'running curl'
curl localhost:1000/newCasesPeak?country=israel