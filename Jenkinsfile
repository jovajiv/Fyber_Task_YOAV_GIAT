pipeline {
    agent { docker { image 'python:3.5.1'
                     args '-p 2000:8080'} }
    stages {
            stage("parameterized _Input") {
            steps {
                script {


                    properties([[$class: 'JiraProjectProperty'], parameters([string(defaultValue: '', description: '''accepts a list of countries seperated by \',\'
                    for example ,
                    israel,australia,austria''', name: 'country', trim: false)])])


                    arr=params.country.tokenize(',')

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
                    pip install pytest --user
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
                    sh 'python -m unittest hello.py'
                    echo "accessing peak cases in country: ${params.country}"
                    echo "accessing peak cases in country: ${arr[0]}"
                    sh "curl localhost:8080/newCasesPeak?country=${params.country}"
                    sh "curl localhost:8080/recoveredPeak?country=${params.country}"
                    sh "curl localhost:8080/deathsPeak?country=${params.country}"
                    sh "curl localhost:8080/newCasesPeak?country=dfgdfgdfg"
                    sh "curl localhost:8090/neeak?country=${params.country}"
                    sh "curl localhost:8/newCasesPeak?country=dfgdfgdfg"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
