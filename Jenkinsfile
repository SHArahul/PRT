pipeline {
    agent any

    environment {
        AWS_REGION = 'ca-central-1'
        ACCOUNT_ID = '<YOUR_AWS_ACCOUNT_ID>'
        ECR_REPO = "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/flask-eks-repo"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CLUSTER_NAME = 'flask-eks-cluster'
        KUBECONFIG = "${WORKSPACE}/kubeconfig"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SHArahul/PRT.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t flask-eks-app:${IMAGE_TAG} .
                '''
            }
        }

        stage('Authenticate to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region ${AWS_REGION} | \
                    docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    docker tag flask-eks-app:${IMAGE_TAG} ${ECR_REPO}:${IMAGE_TAG}
                    docker push ${ECR_REPO}:${IMAGE_TAG}
                '''
            }
        }

        stage('Configure kubectl') {
            steps {
                sh '''
                    aws eks update-kubeconfig \
                      --region ${AWS_REGION} \
                      --name ${CLUSTER_NAME} \
                      --kubeconfig ${KUBECONFIG}
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh '''
                    sed -i "s|IMAGE_PLACEHOLDER|${ECR_REPO}:${IMAGE_TAG}|g" k8s/deployment.yaml

                    kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/namespace.yaml
                    kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/deployment.yaml
                    kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/service.yaml
                    kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/ingress.yaml
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}