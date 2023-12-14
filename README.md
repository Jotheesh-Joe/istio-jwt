# istio-jwt Repository

This repository contains the source code for a sample application that consists of a UI component, an API component, and Kubernetes configurations.

## Components

### 1. UI (sample-app-ui)

The UI component is a Python Flask application. It uses OAuth authentication with Azure AD. To run the UI:

To build and test the docker image locally

```bash
cd sample-app-ui
# Add the necessary environmental variables in the docker run command
docker build -t sample-app-ui .
docker run -p 5000:8080 sample-app-ui
```

### 2. API (sample-app-api)

The API component is responsible for processing requests from the UI. To run the API:

To build and test the docker image locally

```bash
cd sample-app-api
# Add the necessary environmental variables in the docker run command
docker build -t sample-app-api .
docker run -p 5001:8080 sample-app-api
```

### 3. Helm Configurations (helm folder)

The helm configurations folder contains Istio configuration for validating JWT tokens. Ensure you have Istio installed and configured in your Kubernetes cluster. 
Apply the app-core helm chart first

```bash
cd helm/app-core
helm apply . -f ../common/values.yaml
```

Then apply the below helm charts:

```bash
# Add the necessary environmental variables in the secret section of the yaml
cd helm/ui-app
helm apply . -f ../common/values.yaml

cd ../api-app
helm apply . -f ../common/values.yaml
```

## OAuth Authentication with Azure AD
The UI component authenticates users using OAuth with Azure AD. Make sure to configure your Azure AD application and update the necessary credentials in the UI component.

## Running the Application in kubernetes cluster
Apply the k8s.yaml with required fields updated in secret section
Apply Istio configurations for JWT token validation - please dont forget the update the request authentication section.


## Issues and Support
If you encounter any issues or need support, please create an [issue](https://github.com/Jotheesh-Joe/istio-jwt/issues).



