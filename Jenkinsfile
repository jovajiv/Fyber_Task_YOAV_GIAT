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
                    sh 'python hello.py'
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
    post {
        failure {
            mail to: 'yoavgi12@gmail.com',
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Something is wrong with ${env.BUILD_URL}"
        }
    }
}
