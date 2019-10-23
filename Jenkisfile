#!/usr/bin/env groovy
pipeline {
    agent any
    stages{
        stage ('check git') {
            steps{
                git poll: true, url: 'https://github.com/juaneml/IV_1920_Proyecto.git' 
            }
        }

        stage('dependences'){
            steps{
                sh '''
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('script'){
            steps{
                sh '''
                    cd ./test && pytest -v test.py
                '''
            }
        }
    }

    
}