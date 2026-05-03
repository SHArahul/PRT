# PRT

Solution 1: 

# Flask CI/CD Deployment on AWS EKS using Terraform, Docker, Jenkins, and Kubernetes

## Project Overview

This project provisions AWS infrastructure using Terraform, containerizes a Flask application using Docker, automates CI/CD using Jenkins, and deploys the application to Amazon EKS using Kubernetes manifests.

---

## Architecture

Developer Push → GitHub Repository → Jenkins Pipeline → Docker Build/Test → Amazon ECR → Amazon EKS Deployment

### Components:
- Flask Application
- Docker
- Jenkins
- Terraform
- AWS EKS
- AWS ECR
- AWS VPC
- Kubernetes

---

## Repository Structure

flask-eks-cicd/
│
├── FlaskService.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
│
├── tests/
│   └── test_app.py
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
│
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    └── service.yaml

---

## Prerequisites

Before starting, ensure you have:

### Local Machine / Jenkins Server:
- AWS CLI configured
- Terraform >= 1.5
- Docker
- Jenkins
- kubectl
- Python 3.10+
- Git

### AWS Permissions:
- EKS Full Access
- ECR Full Access
- EC2/VPC Access
- IAM Permissions

---

## Step 1: Clone Repository

```bash
git clone https://github.com/your-org/flask-eks-cicd.git
cd flask-eks-cicd

Step 2: Provision AWS Infrastructure

Navigate to Terraform directory:

cd terraform

Initialize Terraform:

terraform init

Validate configuration:

terraform validate

Plan deployment:

terraform plan

Apply infrastructure:

terraform apply -auto-approve

Resources Created:

VPC

Public/Private Subnets

NAT Gateway

EKS Cluster

EKS Managed Node Group

ECR Repository

Step 3: Configure kubectl for EKS
aws eks update-kubeconfig \
  --region us-east-1 \
  --name flask-eks-cluster

Verify nodes:

kubectl get nodes

Step 4: Jenkins Configuration

Required Jenkins Plugins:

Pipeline

Docker Pipeline

AWS Credentials

Git

Kubernetes CLI

Add Credentials:
AWS Access Key
AWS Secret Key

GitHub Credentials

Step 5: Jenkins Pipeline Flow

Pipeline Stages:

Checkout source code

Install dependencies

Run unit tests

Build Docker image

Authenticate with ECR

Push image to ECR

Update kubeconfig

Deploy to EKS

Step 6: Build and Test Locally (Optional)

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest tests/

Expected result:

3 passed

Step 7: Docker Build

docker build -t flask-app .

Run locally:

docker run -p 5000:5000 flask-app

Verify:

curl http://localhost:5000/

curl http://localhost:5000/health

Step 8: Kubernetes Deployment

Apply manifests:

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Check resources:

kubectl get all -n flask-app
Step 9: Access Application

If using LoadBalancer:

kubectl get svc -n flask-app

Retrieve external IP and open:

http://<EXTERNAL-IP>
Jenkinsfile Variable Flow
Environment Variables:
AWS_REGION
ACCOUNT_ID
ECR_REPO
IMAGE_TAG
CLUSTER_NAME
Example:
IMAGE_TAG = "${BUILD_NUMBER}"

Each Jenkins run creates a unique Docker image tag.
