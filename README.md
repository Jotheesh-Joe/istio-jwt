# istio-jwt Repository

This repository contains the source code for a sample application that consists of a UI component, an API component, and Kubernetes configurations.

## Components

### 1. UI (sample-app-ui)

The UI component is a Python Flask application. It uses OAuth authentication with Azure AD. To run the UI:

```bash
cd sample-app-ui
# Add any necessary setup steps here
docker build -t sample-app-ui .
docker run -p 5000:5000 sample-app-ui
```

### API (sample-app-api)
The API component is responsible for processing requests from the UI. To run the API:

cd sample-app-api
# Add any necessary setup steps here
docker build -t sample-app-api .
docker run -p 8080:8080 sample-app-api


