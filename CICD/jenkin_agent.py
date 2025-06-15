
#=========================================================
# Example of Docker Agent in a Jenkinsfile
#=========================================================

pipeline {
    agent {
        docker {
            image 'node:16' // Use Node.js 16 Docker image
            args '-u root'  // Optional: Run container as root
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'npm install' // Run commands inside the Node.js container
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
}

#=========================================================
# Stage-Level Docker Agent
#=========================================================

pipeline {
    agent none // No global agent
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'maven:3.8-openjdk-11' // Use Maven image for this stage
                }
            }
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'node:16' // Use Node.js image for this stage
                }
            }
            steps {
                sh 'npm test'
            }
        }
    }
}

#=========================================================
# Using a Dockerfile
#=========================================================

pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile' // Path to the Dockerfile in your repository
            dir 'docker'          // Directory containing the Dockerfile (optional)
            args '-v /tmp:/tmp'   // Optional Docker run arguments
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}

#=========================================================
# Example with Private Registry
#=========================================================

pipeline {
    agent {
        docker {
            image 'my-private-repo/my-image:latest'
            registryUrl 'https://my-private-repo'
            registryCredentialsId 'docker-credentials'
        }
    }
    stages {
        stage('Run') {
            steps {
                sh 'my-command'
            }
        }
    }
}

#=========================================================
# Node-Based Agent
#=========================================================

pipeline {
    agent {
        label 'my-jenkins-node' // Runs on a node labeled 'my-jenkins-node'
    }
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}

#=========================================================
# No Agent (Local Execution)
#=========================================================

pipeline {
    agent none
    stages {
        stage('Example') {
            steps {
                echo 'Running without an agent'
            }
        }
    }
}

#=========================================================
# Kubernetes agent
#=========================================================

pipeline {
    agent {
        kubernetes {
            yaml '''
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: maven
                image: maven:3.8-openjdk-11
                command:
                - sleep
                args:
                - infinity
            '''
        }
    }
    stages {
        stage('Build') {
            steps {
                container('maven') {
                    sh 'mvn clean package'
                }
            }
        }
    }
}

#=========================================================
# Combine Node + Docker Agent at stage lavel
#=========================================================

pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                label 'build-node'
            }
            steps {
                sh 'make build'
            }
        }
        stage('Test') {
            agent {
                docker { image 'node:16' }
            }
            steps {
                sh 'npm test'
            }
        }
    }
}

#=========================================================
# Amazon EC2 Agent
#=========================================================
