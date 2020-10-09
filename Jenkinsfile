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

                    country_list=params.country.tokenize(',')
                }
            }
        }
        stage('Run Flask Server') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    echo 'Building..'
                    sh """
                    pip install flask --user
                    pip install requests --user
                    """
                    withEnv(['JENKINS_NODE_COOKIE =dontkill']) {
                            echo "Running Flask Server in background..."
                            sh "python app.py &"
                            sh "sleep 5"
                    }
                }
            }
        }
        stage('Execute_curl') {
            steps {
                    sh "echo curl requested countries:"
                    traditional_int_for_loop(country_list)



            }
        }
    }
}


def traditional_int_for_loop(country_list) {
    for (int i = 0; i < country_list.size(); i++) {
        echo "starting country: ${country_list[i]}"
        sh "curl localhost:8080/newCasesPeak?country=${country_list[i]}"
        sh "curl localhost:8080/recoveredPeak?country=${country_list[i]}"
        sh "curl localhost:8080/deathsPeak?country=${country_list[i]}"
    }
}

