# Building the Application

Application is packed up and ready to be deployed on any containerized environment. In order to build the Docker image, all that needs to be done is to run the command below.

    docker image -t <IMAGE_NAME> .

The name of the Docker image on the Kubernetes deployment scripts is ``exercise-app``.