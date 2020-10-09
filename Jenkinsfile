pipeline {
    agent { docker { image 'python:3.5.1'
                     args '-p 2000:8080'} }
    stages {
            stage("parameterized _Input") {
            steps {
                script {
                    properties([[$class: 'JiraProjectProperty'], parameters([string(defaultValue: '', description: '''choose country to query our Flask application with.
                    test will return peak values regarding the last 30 days''', name: 'country', trim: false)])])

                }
            }
        }
        stage('Build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    echo 'Building..'
                    sh """
                    pip install flask --user
                    pip install requests --user
                    """
                    withEnv(['JENKINS_NODE_COOKIE =dontkill']) {
                            sh "python app.py &"
                            sh "sleep 5"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                    echo 'Testing.k.'
                    sh 'ls -l'
                    sh 'pwd'
                    sh 'python --version'
                    sh 'python hello.py'
                    sh 'curl localhost:8080'
                    sh 'curl localhost:8080/newCasesPeak?country=israel'
                    sh 'curl localhost:8080/newCasesPeak?country=australia'
                    echo "accessing peak cases in country: ${params.country}"
                    sh "curl localhost:8080/newCasesPeak?country=${params.country}"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
