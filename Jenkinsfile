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
                    sh """
                    env
                    pip install flask --user
                    pip install requests --user
                    """
                    sh 'python --version'
                    sh 'python hello.py'
                    sh 'chmod +x support.sh'
                    sh './support.sh '
                    sh 'curl localhost:1000'
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
