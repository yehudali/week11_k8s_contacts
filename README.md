# week11_k8s_contacts

```mermaid
graph LR
    User((User / Browser))
    
    subgraph "Kubernetes Cluster"
        direction LR
        
        %% API Layer
        ApiService[("API Service<br>(NodePort)<br>Port: 30080")]
        ApiPod["API Pod<br>(FastAPI Container)<br>Port: 8000"]
        
        %% Database Layer
        MongoService[("MongoDB Service<br>(ClusterIP)<br>Port: 27017")]
        MongoPod[("MongoDB Pod<br>(Mongo Container)<br>Port: 27017")]
        
        %% Connections
        ApiService -.->|"Selector: app=api"| ApiPod
        ApiPod -->|"Connects via Host:<br>mongodb-service"| MongoService
        MongoService -.->|"Selector: app=mongodb"| MongoPod
    end

    %% External Connection
    User -->|"HTTP Request<br>GET /contacts"| ApiService

    %% Styling
    style ApiService fill:#6db33f,stroke:#333,stroke-width:2px,color:white
    style MongoService fill:#6db33f,stroke:#333,stroke-width:2px,color:white
    style ApiPod fill:#326ce5,stroke:#333,stroke-width:2px,color:white
    style MongoPod fill:#326ce5,stroke:#333,stroke-width:2px,color:white

    ```