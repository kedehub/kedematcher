1. Build the Docker Image

Navigate to the directory containing kedematcher project and run the following command:

docker build --no-cache -t kedematcher-image:latest -f kedematcher/dockerize/Dockerfile .

docker image inspect kedematcher-image --format '{{.Architecture}}'

2. Run the Docker Container

docker run --rm --name kedematcher-container -v ~/git/kedematcher/docs:/root/.config/KedeGit kedematcher-image:latest identity-merge

