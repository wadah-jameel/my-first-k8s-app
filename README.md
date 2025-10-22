# My First Kubernetes App 🚀

A beginner-friendly Kubernetes deployment project that demonstrates core K8s concepts through a simple Python Flask web application.

## 🎯 Learning Objectives

- Understand Kubernetes Deployments
- Learn about Services and Load Balancing
- Practice with Namespaces
- Implement Health Checks
- Use Resource Management

## 🛠️ Prerequisites

- Docker installed
- Kubernetes cluster (minikube, kind, or cloud provider)
- kubectl configured
- Basic understanding of containers

## 🚀 Quick Start

### 1. Clone and Navigate
```bash
git clone https://github.com/your-username/my-first-k8s-app.git
cd my-first-k8s-app
```

## 📁 Repository Structure
```bash
my-first-k8s-app/
├── README.md
├── app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
└── docs/
    ├── setup.md
    └── troubleshooting.md
```

## 🚀 Step-by-Step Implementation

### Step 1: Create the Application

#### File: app/app.py
```bash
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>Hello from Kubernetes! 🚀</h1>
    <p>Pod Name: {os.environ.get('HOSTNAME', 'Unknown')}</p>
    <p>Version: 1.0</p>
    """

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### File: app/requirements.txt
```bash
Flask==2.3.3
```

#### File: app/Dockerfile
```bash
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Step 2: Kubernetes Configuration Files

#### File: k8s/namespace.yaml
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-first-app
  labels:
    name: my-first-app
```

#### File: k8s/deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-k8s-deployment
  namespace: my-first-app
  labels:
    app: hello-k8s
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-k8s
  template:
    metadata:
      labels:
        app: hello-k8s
    spec:
      containers:
      - name: hello-k8s
        image: your-username/hello-k8s:v1.0
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
```

#### File: k8s/service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-k8s-service
  namespace: my-first-app
  labels:
    app: hello-k8s
spec:
  selector:
    app: hello-k8s
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer
```

### 2. Build Docker Image
```bash
cd app
docker build -t your-username/hello-k8s:v1.0 .
docker push your-username/hello-k8s:v1.0
```
### 3. Deploy to Kubernetes
```bash
# Create namespace
kubectl apply -f k8s/namespace.yaml

# Deploy application
kubectl apply -f k8s/deployment.yaml

# Create service
kubectl apply -f k8s/service.yaml
```

### 4. Verify Deployment
```bash
# Check pods
kubectl get pods -n my-first-app

# Check service
kubectl get svc -n my-first-app

# Get application URL (for minikube)
minikube service hello-k8s-service -n my-first-app --url
```

## 🔍 Key Concepts Explained

### Deployment

    Replicas: We run 3 instances for high availability
    Rolling Updates: Zero-downtime deployments
    Resource Limits: Prevents resource overconsumption


### Service

    Load Balancer: Distributes traffic across pods
    Service Discovery: Provides stable endpoint
    Port Mapping: Maps external port 80 to container port 5000


### Health Checks

    Liveness Probe: Restarts unhealthy containers
    Readiness Probe: Controls traffic routing

## 📊 Useful Commands
```bash
# View pods with more details
kubectl get pods -n my-first-app -o wide

# Check pod logs
kubectl logs -f deployment/hello-k8s-deployment -n my-first-app

# Scale the deployment
kubectl scale deployment hello-k8s-deployment --replicas=5 -n my-first-app

# Port forward for local testing
kubectl port-forward svc/hello-k8s-service 8080:80 -n my-first-app
```
## 🧹 Cleanup
```bash
# Delete all resources
kubectl delete namespace my-first-app
```

## 🐛 Troubleshooting

### Common Issues

####    ImagePullBackOff
          Ensure image exists and is accessible
          Check image name in deployment.yaml

####    CrashLoopBackOff
          Check pod logs: kubectl logs <pod-name> -n my-first-app
          Verify application starts correctly

####    Service Not Accessible
          Check service endpoints: kubectl get endpoints -n my-first-app
          Verify pod labels match service selector

## 📚 Next Steps

    Add ConfigMaps and Secrets
    Implement Ingress for advanced routing
    Add persistent storage with PersistentVolumes
    Set up monitoring with Prometheus
    Implement CI/CD pipeline

## 🤝 Contributing

    1. Fork the repository
    2. Create a feature branch
    3. Make your changes
    4. Submit a pull request

## 📄 License

### This project is licensed under the MIT License.
```bash
## 🎯 Key Learning Points

### What This Project Teaches:

1. **Container Orchestration**: How Kubernetes manages multiple container instances
2. **Service Discovery**: How pods communicate through services
3. **High Availability**: Running multiple replicas for resilience
4. **Health Monitoring**: Using probes to ensure application health
5. **Resource Management**: Setting CPU and memory limits
6. **Namespace Isolation**: Organizing resources logically

### Beginner-Friendly Features:

- **Simple Application**: Basic Flask app that's easy to understand
- **Clear Documentation**: Step-by-step instructions with explanations
- **Practical Examples**: Real commands you can run
- **Troubleshooting Guide**: Common issues and solutions
- **Progressive Learning**: Start simple, then suggest advanced topics

## 💡 Tips for Your GitHub Repository

1. **Use Clear Commit Messages**: Describe what each commit accomplishes
2. **Add Screenshots**: Show the application running in browser
3. **Include a Demo**: Consider adding a GIF showing the deployment process
4. **Tag Releases**: Use semantic versioning (v1.0, v1.1, etc.)
5. **Add Issues Templates**: Help others report problems effectively

This project provides a solid foundation for understanding Kubernetes while being approachable for beginners. The documentation is comprehensive yet easy to follow, making it perfect for your GitHub portfolio!
```

