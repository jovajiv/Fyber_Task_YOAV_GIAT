#!/bin/bash

echo 'running web server in background ...'
python app.py &


echo 'running curl'
curl localhost:8080/newCasesPeak?country=israel