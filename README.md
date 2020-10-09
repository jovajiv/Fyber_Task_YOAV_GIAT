
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Run](#run)


<!-- ABOUT THE PROJECT -->
## About The Project



### Built With
* [Flask](https://flask.palletsprojects.com)
* [Docker](https://www.docker.com)
* [Jenkins](https://www.jenkins.io)


## Getting Started
This project is a flask app written in Python, designed to scrape 3rd party API regarding covid-19.
returns, upon specified query, json info on peak deaths/recovered/new cases regarding requested country in the last 30 days.
also, attached a jenkinsfile with configuration and basic querys for our flask server.
this repo is deisgned for jenkins server, in case you wish to only run flask app , only app.py is requiered

### Installation

1. install Docker according to specified instructions at  [https://docs.docker.com/get-docker/)
2. install Jenkins according to https://www.jenkins.io/doc/book/installing/
3. run jenkins on docker according to the info specified on (2)
4. finish jenkins installation with the post installation wizard https://www.jenkins.io/doc/book/installing/#setup-wizard

```sh
git clone https://github.com/your_username_/Project-Name.git
```
3. Install NPM packages
```sh
npm install
```
4. Enter your API in `config.js`
```JS
const API_KEY = 'ENTER YOUR API';
```
## run
1. your jenkins server is now up and running , log in using http://localhost:8080/
2. start a new job namee "fyber", name it , and choose the 'Pipeline' option
3. scroll down to "Pipelin", and in the drop down replace "Pipeline script" to "Pipeline script from scp".
4. change scm drop down menu to "git", and input this repository https://github.com/jovajiv/Fyber_Task_YOAV_GIAT.git 
5. apply and save
6. now, at http://localhost:8080/job/fyber/ , choose the "build now" option
7. once the execution is complete, refresh the current web page, you know see the option "build with parameters"
8. click "build with parameters", and insert a list of country names you want to query, as specified in the description
9. at the end of the execution, the outputs of the execution are available at the jobs console output , at http://localhost:8080/job/fyber/<build_id>/console



