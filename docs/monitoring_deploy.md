# Setting Up the Monitoring

## Setting up Prometheus

Clone the repository.  

    git clone https://github.com/prometheus-operator/kube-prometheus.git
    cd kube-prometheus

Create namespaces and definitions.   

    kubectl create -f manifests/setup

Once you confirm the operator is running (``kubectl get ns monitoring``), deploy the monitoring stack.  

    kubectl create -f manifests/

Give it few seconds and the pods should start coming online.   

    kubectl get pods -n monitoring
    kubectl get svc -n monitoring

To access the services using port forwarding:   

    kubectl --namespace monitoring port-forward svc/grafana 3000
    kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090
    kubectl --namespace monitoring port-forward svc/alertmanager-main 9093

## Resources
https://computingforgeeks.com/setup-prometheus-and-grafana-on-kubernetes/
https://devopscube.com/setup-prometheus-monitoring-on-kubernetes/
https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/user-guides/getting-started.md