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
                echo 'Testing.k.'
                sh 'ls -l'
                sh 'pwd'
                sh """
                .env/bin/activate
                pip install flask
                """
                sh 'env'
                sh 'whoami'
                sh 'cat /etc/passwd'
                sh 'python --version'
                sh 'python hello.py'
                sh 'python /var/jenkins_home/workspace/Fyber_Task_YOAV_GIAT_master/app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
