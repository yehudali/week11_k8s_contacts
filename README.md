
code
Markdown
download
content_copy
expand_less
# Week 11 Project: Contact Manager API with Kubernetes

---

## 1. Project Description
A REST API service for managing a contact list, built with FastAPI and MongoDB. The application is containerized and orchestrated using Kubernetes Pods and Services.

### API Endpoints
- **GET /contacts** - Get all contacts.
- **POST /contacts** - Create new contact.
- **PUT /contacts/{id}** - Update existing contact.
- **DELETE /contacts/{id}** - Delete contact.

---

## 2. Prerequisites
- Docker & Docker Hub account
- minikube
- kubectl

---

## 3. Setup & Deployment

### Build and Push Image
```bash
docker build -t yehudali/contacts-api:v1 ./app
docker push yehudali/contacts-api:v1
Deploy to Kubernetes
code
Bash
download
content_copy
expand_less
minikube start
kubectl apply -f k8s/mongodb-pod.yaml
kubectl apply -f k8s/mongodb-service.yaml
kubectl apply -f k8s/api-pod.yaml
kubectl apply -f k8s/api-service.yaml
4. Testing Instructions
Step 1: Set API URL

Run this command to automatically capture the API address:

code
Bash
download
content_copy
expand_less
export API_URL=$(minikube service api-service --url)
Step 2: Run CRUD Tests

Copy and paste these commands to test the API:

Create a contact:

code
Bash
download
content_copy
expand_less
curl -X POST $API_URL/contacts -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "phone_number": "050-1234567"}'

Get all contacts:

code
Bash
download
content_copy
expand_less
curl -X GET $API_URL/contacts

Update contact:
(Replace {id} with an actual ID from the Get All result)

code
Bash
download
content_copy
expand_less
curl -X PUT $API_URL/contacts/{id} -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Smith", "phone_number": "050-0000000"}'

Delete contact:

code
Bash
download
content_copy
expand_less
curl -X DELETE $API_URL/contacts/{id}
5. Helpful Commands
Debugging

kubectl get pods - Check if pods are Running.

kubectl get svc - View service status.

kubectl logs api - View API application logs.

Cleanup

kubectl delete -f k8s/ - Removes all deployed resources.

code
Code
download
content_copy
expand_less