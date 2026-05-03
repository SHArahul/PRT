# Blue-Green Deployment on Amazon EKS using Jenkins, Helm, and Terraform

## Overview

This project demonstrates a production-grade Blue-Green deployment strategy for a Node.js application on Amazon EKS.

### Technologies Used

- Terraform → AWS infrastructure provisioning
- Amazon EKS → Kubernetes orchestration
- Helm → Blue/Green Kubernetes deployments
- Jenkins → CI/CD automation
- Docker → Application containerization
- AWS ECR → Image repository
- AWS ALB Ingress → External traffic routing

---

# Project Structure

```bash
blue-green-eks-nodejs/
│
├── app/                    # Sample Node.js application
│   ├── server.js
│   ├── package.json
│   └── Dockerfile
│
├── terraform/              # EKS, VPC, IAM, ECR provisioning
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── helm/nodejs-app/        # Helm deployment charts
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── values-blue.yaml
│   ├── values-green.yaml
│   └── templates/
│
├── Jenkinsfile             # CI/CD pipeline
└── README.md
```bash


---
Deployment Workflow


cd terraform
terraform init
terraform apply -auto-approve


---
Configure kubectl
aws eks update-kubeconfig --region us-east-1 --name bluegreen-eks
Deploy Initial Blue Environment
helm install nodejs-app ./helm/nodejs-app \
-f ./helm/nodejs-app/values-blue.yaml

---


Blue-Green Release Process
Jenkins builds Docker image
Pushes image to AWS ECR
Detects active environment
Deploys new version to inactive environment
Runs health checks
Switches service traffic
Keeps previous version for rollback


---

Rollback Strategy
Immediate Traffic Rollback
kubectl patch svc nodejs-service \
-p '{"spec":{"selector":{"app":"nodejs-app","version":"blue"}}}'

or

kubectl patch svc nodejs-service \
-p '{"spec":{"selector":{"app":"nodejs-app","version":"green"}}}'
Helm Rollback
helm rollback nodejs-app <revision>
