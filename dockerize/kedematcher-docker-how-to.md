1. Build the Docker Image

Navigate to the directory containing kedematcher project and run the following command:
```
docker build --no-cache -t kedematcher-image:latest -f kedematcher/dockerize/Dockerfile .
```

```
docker image inspect kedematcher-image --format '{{.Architecture}}'
```

2. Run the Docker Container
```
docker run --rm --name kedematcher-container -v ~/git/kedematcher/docs:/root/.config/KedeGit kedematcher-image:latest identity-merge
```
3. Tag your image so you can push the image to this repository:
```
docker tag kedematcher-image:latest public.ecr.aws/kedehub/kedematcher-image:latest
```
 Retrieve an authentication token and authenticate your Docker client to your registry.

```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/kedehub
```

Push your architecture-specific images to ECR (assuming you've already built them):

```
docker push public.ecr.aws/kedehub/kedematcher-image:latest
```


