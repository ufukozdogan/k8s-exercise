# Deploying the Application

After setting up the Kubernetes infrastructure, the deployment file that is needed for the application(``deployment.yaml``) can be found in the ``kubernetes`` folder of this project.

To deploy the application it simply needs to be executed on the Kubernetes master.

    kubectl apply -f deployment.yaml