# Bootstrapping a Kubernetes Environment with Kind

## Kubernetes Setup with Kind

Install Go, Docker and Kind. For more information check out [this](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) link.

After installing them, run the command below to create the Kubernetes distribution:

    kind create cluster

## Ingress Setup
After installing the cluster, to setup the NGINX ingress:

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

Wait until is ready to process requests running: 

    kubectl wait --namespace ingress-nginx \
    --for=condition=ready pod \
    --selector=app.kubernetes.io/component=controller \
    --timeout=90s

## Application Setup

To deploy the application and ingress, execute the commands below.

    kubectl apply -f deployment.yaml
    kubectl apply -f ingress.yaml

## Resources
[Kind Docs](https://kind.sigs.k8s.io/)   
[Kind Configuration](https://kind.sigs.k8s.io/docs/user/ingress/#ingress-nginx)