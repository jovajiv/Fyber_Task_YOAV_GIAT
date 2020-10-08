pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    echo 'Testing.k.'
                    sh 'ls -l'
                    sh 'pwd'
                    sh 'python --version'
                    sh 'pip install Flask'
                    sh 'python /var/jenkins_home/workspace/Fyber_Task_YOAV_GIAT_master/app.py'
                    }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
