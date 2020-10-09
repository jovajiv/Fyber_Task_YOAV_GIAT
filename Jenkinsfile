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
                    sh 'curl localhost:8080'
                    sh 'curl localhost:8080/newCasesPeak?country=israel'
                    sh 'curl localhost:8080/newCasesPeak?country=australia'
                    echo "checking 3rd party api server status: "
                    sh "curl localhost:8080/status"
                    traditional_int_for_loop(country_list)



            }
        }
    }
}


                    def traditional_int_for_loop(country_list) {
                        sh "echo curl requested countries:"
                        for (int i = 0; i < country_list.size(); i++) {
                            echo "starting country: ${country_list[i]}"
                            sh "curl localhost:8080/newCasesPeak?country=${country_list[i]}"
                            sh "curl localhost:8080/recoveredPeak?country=${country_list[i]}"
                            sh "curl localhost:8080/deathsPeak?country=${country_list[i]}"
                        }
                    }